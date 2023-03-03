#this script changes a CSV file into a New JSON file then asks you where to save it
#this script is for a CSV file that has a column for song name and a column for artist name

import csv
import json
import sys

#read CSV file
def read_csv (csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

#create Song Name and Artist Name objects in the JSON file
def create_song_artist(name, artist):
    song = {}
    song['name'] = name
    song['artist'] = artist
    return song

#write JSON file
def write_json(json_file, data):
    with open(json_file, 'w') as fw:
        json.dump(data, fw, indent=4)

#main function
def main():

    data = []
    csv_file = 'Rep_List.csv'
    json_file = 'Rep_List.json' 
    for row in read_csv(csv_file):
        name, artist = row[0],row[1]
        song = create_song_artist(name, artist)
        data.append(song)

    write_json(json_file, data)
    
if __name__ == '__main__':
    main()

    sys.exit()

    