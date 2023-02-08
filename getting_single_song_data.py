import json
from bs4 import BeautifulSoup
import requests

# Make a request to the website's HTML
url = "https://tabs.ultimate-guitar.com/tab/misc-traditional/bingo-chords-1408664"
response = requests.get(url)
html = response.content

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find the specified div with class "js-store"
div = soup.find("div", {"class": "js-store"})

# This points us at the big lump of song data and metadata: first parse it into json

jsonData = json.loads(div.attrs["data-content"])

# Now point at the particular piece we want: it's deeply, deeply nested!!
print(jsonData["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"])
