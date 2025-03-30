import datetime
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv(
    'C:\\githubb\\.venv\\spotify1\\_testfiles\\filtered_data.csv')



# import os
# import glob
# import pandas as pd
# import numpy as np

# relative_path = os.path.join('c:\\githubb\\.venv\\spotify1', '_testfiles', '*.json')
# files = glob.glob(relative_path)

# columns_to_exclude = [
#     'username', 'platform', 'conn_country', 'ip_addr_decrypted',
#     'user_agent_decrypted', 'episode_name', 'episode_show_name',
#     'spotify_episode_uri', 'reason_start', 'reason_end', 'shuffle',
#     'skipped', 'offline', 'offline_timestamp', 'incognito_mode'
# ]

# if not files:
#     print(f"No JSON files found in the specified directory: {relative_path}")
# else:
#     df = pd.concat(map(pd.read_json, files))

#     columns_to_keep = [col for col in df.columns if col not in columns_to_exclude]
#     df_filtered_columns = df[columns_to_keep]
#     df_songs_only = df_filtered_columns[df_filtered_columns['master_metadata_track_name'].notnull()]
#     df_filtered_ms_played = df_songs_only[df_songs_only['ms_played'] >= 10000]

#     if df_filtered_ms_played['ms_played'].dtype != 'int64':
#         df_filtered_ms_played['ms_played'] = pd.to_numeric(df_filtered_ms_played['ms_played'], errors='coerce').fillna(0).astype(int)

#     csv_filename = 'filtered_data.csv'
#     df_filtered_ms_played.to_csv(csv_filename, index=False)
#     print(f"Successfully converted JSON files to CSV (filtered columns, songs, and ms_played): {csv_filename}")