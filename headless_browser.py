#this script navigates to a link, looks at the html of song lists with 'requests' and 'beautiful soup'
#and finds song list from Xpath
#and randomly selects 5 songs from the list and prints them to the screen with the attached URL

import requests
from bs4 import BeautifulSoup
import random
import time
import json

url = "https://www.ultimate-guitar.com/user/playlist/shared?h=ygRmx0t566TJbaT3nybjHh_y"

#open file to write to
f = open("song_list.txt", "w")

#request url
response = requests.get(url)
html = response.content

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find the specified div with class "js-store"
div = soup.find("div", {"class": "js-store"})

# This points us at the big lump of song data and metadata: first parse it into json
jsonData = json.loads(div.attrs["data-content"])

#print json data to f
print(jsonData, file=f)


# Now point at the particular piece we want: it's deeply, deeply nested!!
content = jsonData["store"]["page"]["data"]['songbook']['name']

song_list = jsonData["store"]["page"]["data"]['songbook']['tabs'][0]

#request length of list in json
length = len(jsonData["store"]["page"]["data"]['songbook']['tabs'])
print(length)

#randomly select 5 numbers between 0 and length of list
random_songs = random.sample(range(length), 5)

#loop through random_songs and print the song name and artist to the screen
#for song in random_songs:
   # print(jsonData["store"]["page"]["data"]['songbook']['tabs'][song]['song_name'])
   # print(jsonData["store"]["page"]["data"]['songbook']['tabs'][song]['artist_name'])
   # print(jsonData["store"]["page"]["data"]['songbook']['tabs'][song]['tab_url'])

print(song_list)

print(content)  

print(random_songs)

print ('done')






