import requests
from bs4 import BeautifulSoup
import re

# Function to perform Google search and fetch first result link
def google_search(artist, song):
    search_query = f"{artist} {song} Genius"
    search_url = f"https://www.google.com/search?q={'+'.join(search_query.split())}"
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Google search results: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    result_divs = soup.find_all('div', class_='g', limit=3)
    
    links = []
    for div in result_divs:
        result_link = div.find('a', href=True)
        if result_link:
            links.append(result_link['href'])
    
    return links

# Function to extract tags from HTML content
def extract_tags(song_page_url):
    try:
        response = requests.get(song_page_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Song Tags from {song_page_url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the div containing tags
    tags_div = soup.find('div', class_='SongTags__Container-xixwg3-1 bZsZHM')
    if tags_div:
        tags = []
        # Find all <a> tags within the div
        tag_links = tags_div.find_all('a', class_='SongTags__Tag-xixwg3-2')
        for tag in tag_links:
            tag_name = tag.text.strip()
            tags.append(tag_name)
        return tags
    return []

# Function to clean up the lyrics
def cleanup_lyrics(lyrics):
    # Combine lines within brackets into a single line
    lyrics = re.sub(r'\[\s*([^\]]+?)\s*\]', lambda m: f'[{m.group(1).replace("\n", " ").strip()}]', lyrics)
    
    # Preserve section headers and content in brackets and parentheses
    lyrics = re.sub(r'\[\s*([^\]]+?)\s*\]', r'\n[\1]\n', lyrics)  # Ensure section headers are on their own lines with line breaks
    lyrics = re.sub(r'\(\s*([^\)]+?)\s*\)', r'(\1)', lyrics)  # Clean up parentheses
    
    # Remove excessive line breaks and merge lines within verses
    lines = lyrics.split('\n')
    cleaned_lines = []
    
    in_verse = False
    first_header = True  # Track if it's the first header
    
    for line in lines:
        line = line.strip()
        if re.match(r'\[.*?\]', line) or re.match(r'\(.*?\)', line):
            # Preserve headers and single parentheses/brackets
            if not first_header:
                cleaned_lines.append('')  # Add an extra blank line before headers (except the first one)
            cleaned_lines.append(line)
            first_header = False
            in_verse = False
        elif line:
            if not in_verse:
                cleaned_lines.append('')  # Add a blank line before new verse
                in_verse = True
            cleaned_lines.append(line)
        else:
            in_verse = False
    
    cleaned_lyrics = '\n'.join(cleaned_lines).strip()
    
    return cleaned_lyrics

# Function to get Song Lyrics
def get_song_lyrics(song_page_url):
    try:
        response = requests.get(song_page_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching lyrics from {song_page_url}: {e}")
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract lyrics from the relevant tags
    lyrics = []
    for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
        text = tag.get_text(strip=True, separator='\n')
        if text:
            lyrics.append(text)

    # Join the lines to get the full lyrics as a single string
    full_lyrics = '\n'.join(lyrics)
    
    # Clean up the lyrics
    cleaned_lyrics = cleanup_lyrics(full_lyrics)
    
    return cleaned_lyrics
