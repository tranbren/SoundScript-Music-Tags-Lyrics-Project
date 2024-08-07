from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .genius import google_search, extract_tags, get_song_lyrics
from .models import SearchHistory

@api_view(['POST'])
@permission_classes([AllowAny])
def song_tags(request):
    artist = request.data.get('artist')
    song = request.data.get('song')

    if not artist or not song:
        return Response({'error': 'Artist and song title are required.'}, status=400)

    # Search for the top URLs related to the song
    song_urls = google_search(artist, song)

    if not song_urls:
        return Response({'error': 'Song page not found.'}, status=404)

    # Try extracting tags and lyrics from each URL
    for song_url in song_urls:
        tags = extract_tags(song_url)
        lyrics = get_song_lyrics(song_url)

        # Return tags and lyrics if found
        if tags or lyrics:
            # Save search history
            SearchHistory.objects.create(artist=artist, song=song)
            return Response({'Tags': tags, 'Lyrics': lyrics})

    # If no tags or lyrics are found from any URL
    return Response({'error': 'Tags or Lyrics not found.'}, status=404)
