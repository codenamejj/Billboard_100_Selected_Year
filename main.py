from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=URL)
webs = response.text

soup = BeautifulSoup(webs, "html.parser")

top_song = soup.find(name="h3", class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color"
                                       "-black u-color-white@mobile-max lrv-u-margin-r-150")

other_songs = soup.find_all(name="h3",
                            class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size"
                                   "-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max "
                                   "a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
top_song_list = []
for top in top_song:
    top_song_list.append(top.text.strip())

other_songs_list = []
for songs in other_songs:
    other_songs_list.append(songs.text.strip())

while "" in top_song_list:
    top_song_list.remove("")

song_100_list = top_song_list + other_songs_list
print(song_100_list)
