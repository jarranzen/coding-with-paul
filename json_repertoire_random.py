#this script reads a json file, and randomly selects 5 songs from the list and prints them to the screen without json formatting

import json
import random

with open('CSV_to_Json/Rep_List.json') as repertoire_file:
    repertoire = json.load(repertoire_file)

#randomly select 5 songs from the repertoire
random_songs = random.sample(repertoire, 5)

#loop through the random songs and print them to the screen
for song in random_songs:
    print(song)






