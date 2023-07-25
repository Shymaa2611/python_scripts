import pytube

print("download video from internet using python")
url=input("Enter video url : ")
pytube.YouTube(url).streams.get_highest_resolution().download('Desktop')