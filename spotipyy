import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
import time
from dotenv import load_dotenv
#from spotify1.panda import get_artist_genres


load_dotenv()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri='https://github.com/Adityaa-patel/spotify1',
    scope='user-read-currently-playing user-read-playback-state'))

output_file_path = 'C:\\githubb\\.venv\\spotify1\\output.csv'

# check if csv file exists if not it makaaes one
if not os.path.exists(output_file_path):
    df = pd.DataFrame(columns=['ts', 'ms_played', 'master_metadata_track_name',
                               'master_metadata_album_artist_name', 'master_metadata_album_album_name',
                               'spotify_track_uri','genre', 'reason_start', 'reason_end', 'offline_timestamp'])
    df.to_csv(output_file_path, index=False)

def log_currently_playing():
    last_track_id = None
    last_track_start_time = None
    last_track_logged = None

    while True:
        # Fetch currently playing track
        current_track = sp.current_user_playing_track()

        if current_track is not None and current_track['is_playing']:
            track_id = current_track['item']['id']
            track_name = current_track['item']['name']
            album_name = current_track['item']['album']['name']
            artists = ', '.join([artist['name'] for artist in current_track['item']['artists']])
            timestamp = pd.to_datetime(current_track['timestamp'], unit='ms')
            spotify_uri = current_track['item']['uri']
            reason_start = 'unknown'
            reason_end = 'endplay'

            if track_id != last_track_id:
                # Calculate and update ms_played for the previous track
                if last_track_id is not None and last_track_start_time is not None:
                    ms_played = current_track['timestamp'] - last_track_start_time
                    # Update the previous entry in the CSV with ms_played
                    if last_track_logged is not None:
                        last_track_logged['ms_played'] = ms_played
                        df = pd.DataFrame([last_track_logged])
                        df.to_csv(output_file_path, mode='a', header=False, index=False)
                        print(f"Updated ms_played for the previous track: {ms_played} ms")

                # Log the new track
                new_entry = {
                    'ts': timestamp,
                    'ms_played': 0,  # Placeholder, updated when track changes or stops
                    'master_metadata_track_name': track_name,
                    'master_metadata_album_artist_name': artists,
                    'master_metadata_album_album_name': album_name,
                    'spotify_track_uri': spotify_uri,
                    'reason_start': reason_start,
                    'reason_end': reason_end,
                    'offline_timestamp': 0  # Placeholder for offline timestamp
                }

                print(f"Logged: {track_name} by {artists} at {timestamp}")

                # Update last track variables
                last_track_id = track_id
                last_track_start_time = current_track['timestamp']
                last_track_logged = new_entry

        elif last_track_id is not None:
            # Calculate and update ms_played for the last track when playback stops
            if last_track_start_time is not None:
                ms_played = int(time.time() * 1000) - last_track_start_time
                if last_track_logged is not None:
                    last_track_logged['ms_played'] = ms_played
                    df = pd.DataFrame([last_track_logged])
                    df.to_csv(output_file_path, mode='a', header=False, index=False)
                    print(f"Updated ms_played for the previous track: {ms_played} ms")
            last_track_id = None
            last_track_start_time = None
            last_track_logged = None
            print("Playback stopped or track skipped.")

        else:
            print("No track is currently playing.")

        time.sleep(10)  # Check every 10 seconds
log_currently_playing()

current_track = sp.current_user_playing_track()
#print(current_track)
#print(current_track['item']['artists']) # there is a dictionary which has multiple stuff, item has all we need it has artists which is of type list and then the list only has 1 element which is of type dict with info about artist, but when multoplw artist it'll have multiple elements
# print(get_artist_genres(current_track['item']['artists'][0]['name']))

# def get_artist_genres(artist_name):
#     try:
#         results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
#         if results['artists']['items']:
#             return results['artists']['items'][0]['genres']
#         else:
#             return None
#     except Exception as e:
#         print(f"Error fetching genres for {artist_name}: {e}")
#         return None


#
#
#NOTHING WORKS 
#
#
#

def get_artist_name_list():
    current_track = sp.current_user_playing_track()
    return list(lambda x: current_track['item']['artists'][x]['name'] )

# def get_artist_genres_when_multiple(song_name):
#     try:
#         for i in song_name:
#             print(i['name'])
#     #         results = sp.search(q=f'artist:{i['name']}', type='artist', limit=1)
#     #         if results['artists']['items']:
#     #             return results['artists']['items'][0]['genres']
#     #         else:
#     #             return None
#     except Exception as e:
#         print(f"Error fetching genres for {song_name}: {e}")
#         return None
# print('kkkkk')
print(get_artist_name_list())