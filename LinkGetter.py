from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Initiate headless mode to not open a browser
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

# Link to playlist
PlaylistLink = "https://www.youtube.com/playlist?list=PL6dVz1zQldGT4OLCZPK3MHE5u1qidHENS"
driver.get(PlaylistLink)
elem = driver.find_elements(By.XPATH, "//*[@href]")
linkList = []
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
print(len(linkList))
