from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from pytube import YouTube

# Initiate headless mode to not open a browser
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

# Link to playlist
PlaylistLink = input("YouTube playlist to convert: ")
driver.get(PlaylistLink)

# Finds all href information in html (links)
elem = driver.find_elements(By.XPATH, "//*[@href]")
linkList = []

# Filters the links for videos and duplicates and adds links to linkList
num = 0
for links in elem:
    temp = links.get_attribute("href")
    if temp.find("/watch?v=") > 0:
        temp = temp[0:temp.find("&")]
        for link in linkList:
            if link == temp:
                num = -1
                break
        if num == 0:
            linkList.append(temp)
        num = 0

# make a new folder in downloads
# change this to your download folder path
path = "C:\\Users\\monke\\Downloads\\Mp3 Music"
directoryName = input("Enter the name of the playlist: ")
destination = os.path.join(path, directoryName)

# downloads links (from: https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/#)
for links in linkList:
    yt = YouTube(links)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print("\"" + yt.title + "\"" + " has been successfully downloaded.")
