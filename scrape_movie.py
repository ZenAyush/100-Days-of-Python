import requests
from bs4 import BeautifulSoup
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)


URL = "https://animeindia.in/*"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
all_animes = soup.find_all(name="h3")
anime_titles = [anime.getText() for anime in all_animes]


top_anime = []
for anime in anime_titles:
    if anime == "Share":
        break
    else:
        top_anime.append(anime)

top_anime = top_anime[::-1]
print(top_anime)

with open ("anime.txt", mode="w") as file:
    for anime in top_anime:
        file.write(f"{anime}\n")