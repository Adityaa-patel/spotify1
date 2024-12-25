from collections import Counter
from file_input import songsss
from datetime import date

def top_monthly(date_time=None, n=5):
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


def top_specified(date_start=None, date_end=None , n =5):
    if date_start is not None and date_end is not None:
        sourcefile = list(filter(lambda x: date.fromisoformat(date_start) <= date.fromisoformat(x[4]) <= date.fromisoformat(date_end), songsss))
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


def count_song(song_id):
    return len(list(filter(lambda x: x == song_id, map(lambda x: x[3], songsss))))

def total_(date_time=None):
    if date_time is not None:
        sourcefile = list(filter(lambda x: x[4][:7] == date_time, songsss))
    else:
        sourcefile = songsss
    return sum(map(lambda x: int(x[5]), sourcefile))

