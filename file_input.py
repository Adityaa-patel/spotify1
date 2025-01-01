import json

def data_extract(content_):
    extracted_data = []
    for i in content_:
        if i['master_metadata_track_name'] is not None:
            extracted_data.append([i["master_metadata_track_name"],i["master_metadata_album_artist_name"],i["master_metadata_album_album_name"],i["spotify_track_uri"][14:],i['ts'][:10],i['ms_played'],i["skipped"],i['reason_start']])
    return extracted_data

with open(r'.venv\spotify1\_testfiles\Streaming_History_Video_2022-2024.json', 'r', encoding='utf-8') as file:
    content1 = json.load(file) # content is in list format
with open(r'.venv\spotify1\_testfiles\Streaming_History_Video_2022-2024.json', 'r', encoding='utf-8') as file:
    content2 = json.load(file)
with open(r'.venv\spotify1\_testfiles\Streaming_History_Video_2022-2024.json', 'r', encoding='utf-8') as file:
    content3 = json.load(file)
with open(r'.venv\spotify1\_testfiles\Streaming_History_Video_2022-2024.json', 'r', encoding='utf-8') as file:
    content4 = json.load(file)
with open(r'.venv\spotify1\_testfiles\Streaming_History_Video_2022-2024.json', 'r', encoding='utf-8') as file:
    content5 = json.load(file)
songsss=data_extract(content1)+data_extract(content2) + data_extract(content3)+data_extract(content4)+data_extract(content5)

print(songsss[1])
# import os
# import glob
# import json

# def data_extract(content_):
#     extracted_data = []
#     for i in content_:
#         if i['master_metadata_track_name'] is not None:
#             extracted_data.append([
#                 i["master_metadata_track_name"],
#                 i["master_metadata_album_artist_name"],
#                 i["master_metadata_album_album_name"],
#                 i["spotify_track_uri"][14:],
#                 i['ts'][:10],
#                 i['ms_played'],
#                 i["skipped"],
#                 i['reason_start']
#             ])
#     return extracted_data

# # Define the relative path to the directory
# relative_path = os.path.join('c:\\githubb\\.venv\\spotify1', '_testfiles', '*.json')

# # Get a list of all JSON files in the directory
# files = glob.glob(relative_path)

# if not files:
#     print(f"No JSON files found in the specified directory: {relative_path}")
# else:
#     all_data = []
#     for file in files:
#         with open(file, 'r', encoding='utf-8') as f:
#             content = json.load(f)
#             all_data.extend(data_extract(content))  # Append extracted data to the list

#     # `all_data` now contains the combined data from all JSON files
#     print(f"Processed {len(files)} files. Extracted {len(all_data)} entries.")

# print(content[1])