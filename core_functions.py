from collections import Counter

def data_extract(content_):
    extracted_data = []
    for i in content_:
        if i['master_metadata_track_name'] is not None:
            extracted_data.append([i["master_metadata_track_name"],i["master_metadata_album_artist_name"],i["master_metadata_album_album_name"],i["spotify_track_uri"][14:],i['ts'][:9],i['ms_played'],i["skipped"],i['reason_start']])
    return extracted_data

def top(songsss, date_time=None, n=5):
    if date_time is not None:
        sourcefile = list(filter(lambda x: x[4][:7] == date_time, songsss))
    else:
        sourcefile = songsss
    type_ = input('Type (songs/artists/albums/song_ids): ').lower()
    if type_ == 'songs':
        q = 0
    elif type_ == 'artists':
        q = 1
    elif type_ == 'albums':
        q = 2
    elif type_ == 'song_ids':
        q = 3
    else:
        print('Invalid type')
        return
    counter = Counter(map(lambda x: x[q], sourcefile))
    return counter.most_common(n)

def count_song(songsss, song_id):
    return len(list(filter(lambda x: x == song_id, map(lambda x: x[3], songsss))))

def total_(songsss, date_time=None):
    if date_time is not None:
        sourcefile = list(filter(lambda x: x[4][:7] == date_time, songsss))
    else:
        sourcefile = songsss
    return sum(map(lambda x: int(x[5]), sourcefile))
