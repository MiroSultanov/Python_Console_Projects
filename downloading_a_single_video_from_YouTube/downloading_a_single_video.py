# 1. # importing the module
from pytube import YouTube

# 2. where to save
SAVE_PATH = "D:\Videos\Youtube_Videos"

# 3. link of the video to be downloaded
link = 'https://www.youtube.com/watch?v=dbkpcfX54gg'

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")

# 4. filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

# 5. to set the name of the file
yt.set_filename('GeeksforGeeks Video')

# 6. get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
    # 7. downloading the video
    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')

