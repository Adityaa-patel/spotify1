import pandas as pd
import glob
import os

# Get the directory where the script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)
#Construct the relative path to the _testfiles directory
relative_path = os.path.join('c:\githubb\.venv\spotify1', '_testfiles', '*.json')

files = glob.glob(os.path.join('c:\githubb\.venv\spotify1', '_testfiles', '*.json'))

if not files:
    print(f"No JSON files found in the specified directory: {relative_path}")
else:
    df = pd.concat(map(pd.read_json, files))
df=df[['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','master_metadata_album_album_name','spotify_track_uri','reason_start','reason_end','offline_timestamp']]

songs_only_df = df.query('master_metadata_track_name != None')
print(songs_only_df.dtypes)
