from pytube import Playlist
import eyed3
import os

# make a new folder in downloads
# change this to your download folder path
path = "C:\\Users\\monke\\Downloads\\Mp3 Music"
directoryName = input("Enter the name of the playlist: ")
destination = os.path.join(path, directoryName)

playlist = Playlist('https://music.youtube.com/playlist?list=PL6dVz1zQldGT4OLCZPK3MHE5u1qidHENS')
for video in playlist.videos:
    videoSettings = video.streams.filter(only_audio=True).first()

    # download the file
    out_file = videoSettings.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print("\"" + video.title + "\"" + " has been successfully downloaded.")

    # change metadata
    audiofile = eyed3.load(base + '.mp3')


