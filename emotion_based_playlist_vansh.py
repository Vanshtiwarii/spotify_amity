# # Import necessary libraries
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from textblob import TextBlob
# import streamlit as st
# import random

# # Spotify API setup
# CLIENT_ID = 'your_client_id'
# CLIENT_SECRET = 'your_client_secret'
# REDIRECT_URI = 'http://localhost:8888/callback'

# # Authenticate Spotify API client
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
#                                                client_secret=CLIENT_SECRET,
#                                                redirect_uri=REDIRECT_URI,
#                                                scope="user-library-read playlist-read-private"))

# # Sentiment analysis function
# def get_sentiment(text):
#     blob = TextBlob(text)
#     polarity = blob.sentiment.polarity
    
#     if polarity > 0.2:
#         sentiment = 'happy'
#     elif polarity < -0.2:
#         sentiment = 'sad'
#     elif polarity > 0:
#         sentiment = 'excited'
#     elif polarity < -0.5:
#         sentiment = 'angry'
#     else:
#         sentiment = 'relaxed'
    
#     return sentiment

# # Playlist function based on sentiment
# def get_playlist_for_sentiment(sentiment):
#     playlists = {
#         'happy': ['https://open.spotify.com/playlist/3bQy66sMaRDIUIsS7UQnuO',  # Happy Hits
#                   'https://open.spotify.com/playlist/6CoCkAYfwWnOynMwhHZHNU'],  # Pop Hits
#         'sad': ['https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT',  # Sad Songs
#                 'https://open.spotify.com/playlist/4YOfhHpjPB0tq29NPpDY3F'],  # Lonely Songs
#         'excited': ['https://open.spotify.com/playlist/3fe6tXjp8x87sMLffEie2Q',  # Workout Playlist
#                     'https://open.spotify.com/album/3009df4r6StN8TZDN1VYci'],  # Party Playlist
#         'angry': ['https://open.spotify.com/playlist/5cwtgqs4L1fX8IKoQebfjJ',  # Angry Metal
#                   'https://open.spotify.com/playlist/37i9dQZF1DX2SThom9u2re'],  # Metal Hits
#         'relaxed': ['https://open.spotify.com/playlist/37i9dQZF1DX2SThom9u2re',  # Chill Vibes
#                     'https://open.spotify.com/playlist/37i9dQZF1DWX3SoTqhs2rq'],  # Deep Focus
#     }
    
#     return random.choice(playlists.get(sentiment, playlists['relaxed']))  # Default to 'relaxed' playlist

# # Function to fetch user playlists
# def get_user_playlists():
#     playlists = sp.current_user_playlists()
#     playlist_links = []
#     for playlist in playlists['items']:
#         playlist_links.append({
#             'name': playlist['name'],
#             'url': playlist['external_urls']['spotify']
#         })
#     return playlist_links

# # Function to search songs based on a mood
# def search_songs_by_mood(mood):
#     query = f"genre:{mood}"
#     results = sp.search(query, type='track', limit=5)
#     songs = []
#     for track in results['tracks']['items']:
#         songs.append({
#             'name': track['name'],
#             'artist': track['artists'][0]['name'],
#             'url': track['external_urls']['spotify']
#         })
#     return songs

# # Streamlit app interface
# def emotion_based_playlist():
#     st.title("Emotion-Based Playlist Generator")
    
#     # Mood input (user can either type or select)
#     mood_input = st.text_input("Enter your mood or thoughts:", "")
    
#     # Function to recommend playlist based on text input
#     if mood_input:
#         sentiment = get_sentiment(mood_input)
#         playlist_url = get_playlist_for_sentiment(sentiment)
#         st.write(f"Based on your input, we recommend this **{sentiment}** playlist:")
#         st.markdown(f"[Click here to listen to the playlist]({playlist_url})")
        
#         # Search songs based on mood
#         songs = search_songs_by_mood(sentiment)
#         st.write("Here are some songs that match your mood:")
#         for song in songs:
#             st.markdown(f"[{song['name']}]({song['url']}) by {song['artist']}")
    
#     # Option for selecting mood (dropdown)
#     mood_select = st.selectbox(
#         "Or select your mood from the list below:",
#         ["happy", "sad", "excited", "angry", "relaxed"]
#     )
    
#     if mood_select:
#         playlist_url = get_playlist_for_sentiment(mood_select)
#         st.write(f"Based on your selected mood, we recommend this **{mood_select}** playlist:")
#         st.markdown(f"[Click here to listen to the playlist]({playlist_url})")
        
#         # Search songs based on mood
#         songs = search_songs_by_mood(mood_select)
#         st.write("Here are some songs that match your mood:")
#         for song in songs:
#             st.markdown(f"[{song['name']}]({song['url']}) by {song['artist']}")
    
#     # Option to view user's playlists
#     if st.button("View My Playlists"):
#         user_playlists = get_user_playlists()
#         if user_playlists:
#             st.write("Here are your saved playlists:")
#             for playlist in user_playlists:
#                 st.markdown(f"[{playlist['name']}]({playlist['url']})")
#         else:
#             st.write("You don't have any playlists saved yet.")
    
#     # Add a 'Refresh' button for a new recommendation
#     if st.button("Refresh Playlist Recommendation"):
#         new_sentiment = random.choice(['happy', 'sad', 'excited', 'angry', 'relaxed'])
#         new_playlist_url = get_playlist_for_sentiment(new_sentiment)
#         st.write(f"Refreshing... Here's a new **{new_sentiment}** playlist:")
#         st.markdown(f"[Click here to listen to the playlist]({new_playlist_url})")
    
#     # Show mood descriptions
#     st.sidebar.title("Mood Descriptions")
#     st.sidebar.write("""  
#     - **Happy**: Bright and upbeat music to lift your spirits.
#     - **Sad**: Slow and mellow tracks to match a somber mood.
#     - **Excited**: High-energy music to get you moving.
#     - **Angry**: Intense tracks to channel your frustration.
#     - **Relaxed**: Calm, soothing tunes for winding down.
#     """)

# # Run the Streamlit app
# if __name__ == "__main__":
#     emotion_based_playlist()




# Import necessary libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from textblob import TextBlob
import streamlit as st
import random

# Spotify API setup
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8888/callback'

# Authenticate Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read playlist-read-private"))

# Sentiment analysis function
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.2:
        sentiment = 'happy'
    elif polarity < -0.2:
        sentiment = 'sad'
    elif polarity > 0:
        sentiment = 'excited'
    elif polarity < -0.5:
        sentiment = 'angry'
    else:
        sentiment = 'relaxed'
    
    return sentiment

# Playlist function based on sentiment
def get_playlist_for_sentiment(sentiment):
    playlists = {
        'happy': ['https://open.spotify.com/playlist/3bQy66sMaRDIUIsS7UQnuO',  # Happy Hits
                  'https://open.spotify.com/playlist/6CoCkAYfwWnOynMwhHZHNU'],  # Pop Hits
        'sad': ['https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT',  # Sad Songs
                'https://open.spotify.com/playlist/4YOfhHpjPB0tq29NPpDY3F'],  # Lonely Songs
        'excited': ['https://open.spotify.com/playlist/3fe6tXjp8x87sMLffEie2Q',  # Workout Playlist
                    'https://open.spotify.com/album/3009df4r6StN8TZDN1VYci'],  # Party Playlist
        'angry': ['https://open.spotify.com/playlist/5cwtgqs4L1fX8IKoQebfjJ',  # Angry Metal
                  'https://open.spotify.com/playlist/37i9dQZF1DX2SThom9u2re'],  # Metal Hits
        'relaxed': ['https://open.spotify.com/playlist/37i9dQZF1DX2SThom9u2re',  # Chill Vibes
                    'https://open.spotify.com/playlist/37i9dQZF1DWX3SoTqhs2rq'],  # Deep Focus
    }
    
    return random.choice(playlists.get(sentiment, playlists['relaxed']))  # Default to 'relaxed' playlist

# Streamlit app interface
def emotion_based_playlist():
    st.title("Emotion-Based Playlist Generator")
    
    # Mood input (user can either type or select)
    mood_input = st.text_input("Enter your mood or thoughts:", "")
    
    # Function to recommend playlist based on text input
    if mood_input:
        sentiment = get_sentiment(mood_input)
        playlist_url = get_playlist_for_sentiment(sentiment)
        st.write(f"Based on your input, we recommend this **{sentiment}** playlist:")
        st.markdown(f"[Click here to listen to the playlist]({playlist_url})")
    
    # Option for selecting mood (dropdown)
    mood_select = st.selectbox(
        "Or select your mood from the list below:",
        ["happy", "sad", "excited", "angry", "relaxed"]
    )
    
    if mood_select:
        playlist_url = get_playlist_for_sentiment(mood_select)
        st.write(f"Based on your selected mood, we recommend this **{mood_select}** playlist:")
        st.markdown(f"[Click here to listen to the playlist]({playlist_url})")

    # Add a 'Refresh' button for a new recommendation
    if st.button("Refresh Playlist Recommendation"):
        new_sentiment = random.choice(['happy', 'sad', 'excited', 'angry', 'relaxed'])
        new_playlist_url = get_playlist_for_sentiment(new_sentiment)
        st.write(f"Refreshing... Here's a new **{new_sentiment}** playlist:")
        st.markdown(f"[Click here to listen to the playlist]({new_playlist_url})")
    
    # Show mood descriptions
    st.sidebar.title("Mood Descriptions")
    st.sidebar.write("""
    - **Happy**: Bright and upbeat music to lift your spirits.
    - **Sad**: Slow and mellow tracks to match a somber mood.
    - **Excited**: High-energy music to get you moving.
    - **Angry**: Intense tracks to channel your frustration.
    - **Relaxed**: Calm, soothing tunes for winding down.
    """)

# Run the Streamlit app
if __name__ == "__main__":
    emotion_based_playlist() 
