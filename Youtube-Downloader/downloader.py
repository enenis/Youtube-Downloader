from pytube import Youtube

link=input("Link: ")

yt=Youtube(link)
ys= yt.streams.get_highest_resolution()


print("Downloading....")
ys.download()
print("Downloaded..")
