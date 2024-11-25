# SoundScript - Music Tags and Lyrics Website 🎶

Welcome to SoundScript, a Music Tags and Lyrics Website! This tool allows users to input an artist and song title to find related tags and genres, and fetches song lyrics. Perfect for music enthusiasts and anyone looking to explore more about their favorite songs!

## Features

- **Display Tags/Genres**: Fetch and display tags and genres related to individual songs.
- **Display Lyrics**: Retrieve and show the lyrics of the song from Genius.

## Technology Stack

### Frontend

- **[React](https://reactjs.org/)**: Utilized for building the user interface.
- **[Vite](https://vitejs.dev/)**: For fast and efficient development.
- **[Tailwind CSS](https://tailwindcss.com/)**: For styling and layout.
- **[DaisyUI](https://daisyui.com/)**: For pre-styled UI components.
- **[Lottie Files](https://lottiefiles.com/)**: For Animation components.

### Backend

- **[Django](https://www.djangoproject.com/)**: Python-based framework used for server-side operations and handling API requests.

### Web Scraping

- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)**: Employed for web scraping to gather tags and genres.
- **[Requests](https://docs.python-requests.org/en/latest/)**: Used to make POST requests from the frontend to the backend for data retrieval.

## How It Works

1. **User Input**: Enter an artist and song title on the frontend.
2. **Backend Processing**: The frontend sends a request to the Django backend.
3. **Web Scraping**: Django uses Beautiful Soup to scrape relevant tags and genres from the web.
4. **Lyrics Retrieval**: Fetches song lyrics from Genius using their API.
5. **Display Results**: The backend sends the data back to the frontend, which displays the tags, genres, and lyrics.

### Initial Load In

![Home Screen](https://github.com/tranbren/Music-Tags-Lyrics-Project/blob/main/InitialLoadup.png)

### Tags/Lyrics Display

![Search Results](https://github.com/tranbren/Music-Tags-Lyrics-Project/blob/main/SongEntry.png)
