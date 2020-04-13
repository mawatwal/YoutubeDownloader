from pytube import YouTube
link='https://www.youtube.com/watch?v=pbCw1FD22Bo'
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()

# from pytube import Playlist   # to download complete playlist 
# playlist = Playlist(" ")
# for video in playlist:
#   video.streams.get_highest_resolution().download()

#Youtube('https://www.youtube.com/watch?v=pbCw1FD22Bo').streams[0].download()   # for highest quality video download(720p)

#print(yt.streams)   # for printing all the available streams
#print(yt.streams.filter(progressive=True))  # to view progressive downloading streams; 720p and below
#print(yt.streams.filter(subtype='mp4'))   # to list only mp4 streams
#print(yt.streams.filter(subtype='mp4').filter(progressive=True))   # to list streams using given filter  
#print(yt.streams.get_by_itag(22))   # to list streams by their itag
