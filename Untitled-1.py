import json
from collections import Counter

def data_extract(content_):
   list=[]
   for i in content_:
        if i['master_metadata_track_name']!=None:
            list+=[[i["master_metadata_track_name"],i["master_metadata_album_artist_name"],i["master_metadata_album_album_name"],i["spotify_track_uri"][14:],i['ts'][:9],i['ms_played'],i["skipped"],i['reason_start']]]
   return list

def top(date_time = None,n = 5):
    if date_time != None:
        sourcefile=list(filter(lambda x: x[4][:7] == date_time,songsss))
    elif date_time == None:
        sourcefile=songsss
    type_=(input('type:')).lower()
    if type_=='songs':
        q=0
    elif type_=='artists':
        q=1
    elif type_=='albums':
        q=2
    elif type_=='song_ids':
        q=3
    else:
        print('Invalid type')
        return
    counter = Counter(list(map(lambda x: x[q],sourcefile)))
    return counter.most_common()[:n] 

def count_song(song_id):
    return len((list(filter(lambda x: x==song_id,list(map(lambda x: x[3] ,songsss))))))

def total_(date_time=None):
    if date_time != None:
        sourcefile=list(filter(lambda x: x[4][:7] == date_time,songsss))
    elif date_time == None:
        sourcefile=songsss
    return sum(map(lambda x: int(x[5]) ,sourcefile))

with open(r'\spotify1\Streaming_History_Audio_2021-2023_0.json', 'r', encoding='utf-8') as file:
    content1 = json.load(file) # content is in list format
with open(r'\spotify1\Streaming_History_Audio_2023_1.json', 'r', encoding='utf-8') as file:
    content2 = json.load(file)
with open(r'\spotify1\Streaming_History_Audio_2023-2024_2.json', 'r', encoding='utf-8') as file:
    content3 = json.load(file)
with open(r'\spotify1\Streaming_History_Audio_2024_3.json', 'r', encoding='utf-8') as file:
    content4 = json.load(file)
with open(r'\spotify1\Streaming_History_Audio_2024_4.json', 'r', encoding='utf-8') as file:
    content5 = json.load(file)
songsss=data_extract(content1)+data_extract(content2) + data_extract(content3)+data_extract(content4)+data_extract(content5)

