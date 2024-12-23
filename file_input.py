import json
from collections import Counter
from core_functions import data_extract, top

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

print(top(songsss))