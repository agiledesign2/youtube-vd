# pip install pypiwin32 pytube
import win32clipboard
from pytube import YouTube

#default link
link = "https://www.youtube.com/watch?v=gaPGpUU6jKQ"
try:
    # get clipboard data
    win32clipboard.OpenClipboard()
    link = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()except Exception as ex:
    print('Error : ',e)
    exit()

try:
    #where to save 
    SAVE_PATH = "PATH_TO_STORE_VIDEO"    yt = YouTube(link)
    print('Title :',yt.title)    print('Available formats :')
    for stream in yt.streams.all():
        print(stream)    itag = input('\nEnter the itag number to download video of that format: ')
    stream = yt.streams.get_by_itag(itag)    print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH)    stream.download(SAVE_PATH)
    input('Hit Enter to exit')except Exception as e: 
    print("Error",e) #to handle exception 
    input('Hit Enter to exit')