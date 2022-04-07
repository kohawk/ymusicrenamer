import requests, os
from bs4 import BeautifulSoup

try:
    os.mkdir("renamed")
except FileExistsError:
    pass

directory = os.getcwd()

count = 0

def GetArtistName(number):
    url = f"https://music.yandex.ru/track/{number}"
    RawText = requests.get(url)
    LxmlText = BeautifulSoup(RawText.text, "lxml")
    ArtistName = LxmlText.find("div", "sidebar__info sidebar__info-short").find("a", "d-link deco-link")
    return ArtistName.text

def GetSongTitle(number):
    url = f"https://music.yandex.ru/track/{number}"
    RawText = requests.get(url)
    LxmlText = BeautifulSoup(RawText.text, "lxml")
    SongTitle = LxmlText.find("div", "sidebar__title sidebar-track__title deco-type typo-h2").find("a", "d-link deco-link")
    return SongTitle.text

for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        filename = os.path.splitext(filename)[0]
        os.rename(os.path.join(directory, f"{filename}.mp3"), f"renamed\{GetArtistName(filename)} - {GetSongTitle(filename)}".strip() + ".mp3")
        count += 1

print(f"Renamed {count} songs")
