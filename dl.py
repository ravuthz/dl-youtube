from pytube import YouTube

LINK_PATH = "./links.txt"
SAVE_PATH = "/Users/ravuthz/Downloads/youtubes"

with open(LINK_PATH, 'r') as file:
    for line in file:
        try:
            yt = YouTube(line.strip())
            print('Downloading: ' + yt.title)
        except:
            print("Connection Error")
        # video = yt.streams.filter(progressive=True, file_extension='mp4')
        video = yt.streams.get_highest_resolution()
        # dl_video = yt.get(video[-1].extension, video[-1].resolution)
        try:
            # dl_video.download(SAVE_PATH)
            video.download(SAVE_PATH)
        except:
            print("Download Error!")

print('Task Completed!')
