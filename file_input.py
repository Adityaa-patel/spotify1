import json

def data_extract(content_):
    extracted_data = []
    for i in content_:
        if i['master_metadata_track_name'] is not None:
            extracted_data.append([i["master_metadata_track_name"],i["master_metadata_album_artist_name"],i["master_metadata_album_album_name"],i["spotify_track_uri"][14:],i['ts'][:10],i['ms_played'],i["skipped"],i['reason_start']])
    return extracted_data

with open(r'_testfiles\Streaming_History_Audio_2021-2023_0.json', 'r', encoding='utf-8') as file:
    content1 = json.load(file) # content is in list format
with open(r'_testfiles\Streaming_History_Audio_2023_1.json', 'r', encoding='utf-8') as file:
    content2 = json.load(file)
with open(r'_testfiles\Streaming_History_Audio_2023-2024_2.json', 'r', encoding='utf-8') as file:
    content3 = json.load(file)
with open(r'_testfiles\Streaming_History_Audio_2024_3.json', 'r', encoding='utf-8') as file:
    content4 = json.load(file)
with open(r'_testfiles\Streaming_History_Audio_2024_4.json', 'r', encoding='utf-8') as file:
    content5 = json.load(file)
songsss=data_extract(content1)+data_extract(content2) + data_extract(content3)+data_extract(content4)+data_extract(content5)

