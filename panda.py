import pandas as pd
import glob
import os
import time

time_start = time.time()
relative_path = os.path.join('c:\githubb\.venv\spotify1', '_testfiles', '*.json')

files = glob.glob(os.path.join('c:\githubb\.venv\spotify1', '_testfiles', '*.json'))

if not files:
    print(f"No JSON files found in the specified directory: {relative_path}")
else:
    df = pd.concat(map(pd.read_json, files))
df=df[['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','master_metadata_album_album_name','spotify_track_uri','reason_start','reason_end','offline_timestamp']]
df['ts'] = pd.to_datetime(df['ts'])
songs_only_df = df.query('master_metadata_track_name != None')


