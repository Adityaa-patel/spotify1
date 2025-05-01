import pandas as pd
import glob
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()
spotify = Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                                         client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")))

relative_path = os.path.join('c:\githubb\.venv\spotify1', '_testfiles', '*.json')

files = glob.glob(os.path.join('c:\githubb\.venv\spotify1', '_testfiles', '*.json'))

if not files:
    print(f"No JSON files found in the specified directory: {relative_path}")
else:
    df = pd.concat(map(pd.read_json, files))
df=df[['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','master_metadata_album_album_name','spotify_track_uri','reason_start','reason_end','offline_timestamp']]
df['ts'] = pd.to_datetime(df['ts'])
songs_only_df = df.query('master_metadata_track_name != None and ms_played>1000')

#output_file = 'c:\\githubb\\.venv\\spotify1\\output.csv'
#songs_only_df.to_csv(output_file, index=False)
#print(f"DataFrame saved to")


def get_artist_genres_for_1_artist(artist_name):
    try:
        results = spotify.search(q=f'artist:{artist_name}', type='artist', limit=1)
        if results['artists']['items']:
            return results['artists']['items'][0]['genres']
        else:
            return None
    except Exception as e:
        print(f"Error fetching genres for {artist_name}: {e}")
        return None


