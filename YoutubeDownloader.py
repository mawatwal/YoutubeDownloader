# comment : https://pypi.org/project/pytube/
# comment :install necessary libraries
# comment : pytube - A pythonic library for downloading YouTube Videos.
from pytube import YouTube
# comment : specify the URL of the video to be downloaded
link='https://www.youtube.com/watch?v=pbCw1FD22Bo'
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
# comment : to download complete playlist from the Youtube, un-comment the below lines of code
# from pytube import Playlist    
# playlist = Playlist("enter the starting url of the playlist ")
# for video in playlist:
#   video.streams.get_highest_resolution().download()

# comment: for highest quality video download (generally 720p because the higher versions have been modified by Youtube lately)
# Youtube('https://www.youtube.com/watch?v=pbCw1FD22Bo').streams[0].download()   

# comment : for printing all the available streams with and without different filters
# print(yt.streams)   
#print(yt.streams.filter(progressive=True)) 
#print(yt.streams.filter(subtype='mp4')) 
#print(yt.streams.filter(subtype='mp4').filter(progressive=True))   
#print(yt.streams.get_by_itag(22))
