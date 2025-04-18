import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import sys # Import sys for exiting

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI") #loopback IP

# Check
if not CLIENT_ID or not CLIENT_SECRET:
    print("Error: SPOTIPY_CLIENT_ID or SPOTIPY_CLIENT_SECRET not found in environment variables.")
    print("Please ensure they are set in your .env file or system environment.")
    sys.exit(1) # exits if missing

try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-read-currently-playing user-read-playback-state',
        cache_path=".spotify_token_cache"
    ))
    sp.current_user()
    print("Spotify authentication successful.")

except Exception as e:
    print(f"Error during Spotify authentication: {e}")
    sys.exit(1)