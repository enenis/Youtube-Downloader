from pytube import Youtube

link=input("Link: ")

yt=Youtube(link)
ys= yt.streams.get_highest_resolution()


print("indiriliyor....")
ys.download()
print("indirildi..")