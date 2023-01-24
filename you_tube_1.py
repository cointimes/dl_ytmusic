#coding: utf-8
import webbrowser as wb
from pytube import YouTube
import sys

dl_directory = '../yt_music/'

dl_url = 'https://www.youtube.com/watch?v=Xe0gIFxYhrk'
if len( sys.argv ) != 2:
    dl_url = input('make sure to entry one url >>>')
else :
    dl_url = sys.argv[1]
#print(YouTube(dl_url).streaming_data)

for i in YouTube(dl_url).streams.filter(only_audio=True):
    print(i)
itag_in = "140" #input('enter the number of itag you want to DOWNLOAD >>>')
YouTube( dl_url ).streams.get_by_itag(itag_in).download(dl_directory)

print('DONE')
sys.exit()