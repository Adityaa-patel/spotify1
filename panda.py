import pandas
import json
import time

start=time.time()

df = pandas.DataFrame(columns=('song', 'artist',  'album', 'time', 'duration', 'skipped', 'reasonstart'))
def data_extractv2(content_):
    for i in content_:
        if i['master_metadata_track_name'] is not None:
            df.loc[i["spotify_track_uri"][14:]] = [i["master_metadata_track_name"]]+[i["master_metadata_album_artist_name"]]+[i["master_metadata_album_album_name"]]+[i['ts'][:10]]+[i['ms_played']]+[i["skipped"]]+[i['reason_start']]
    return df

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
songss=data_extractv2(content1)+data_extractv2(content2) + data_extractv2(content3)+data_extractv2(content4)+data_extractv2(content5)

timetaken=time.time()-start

print(songss)
print(timetaken)