# Sound Cloud Scraper
import requests
from bs4 import BeautifulSoup
import re


# User input for artist name/ song name
search_query = input("Enter search query: ")

# Creates an http req and retrieves the url based on the artist/ song name
r = requests.get("https://soundcloud.com/search?q=" + search_query)

# Converts the html request object to a soup object
soup = BeautifulSoup(r.text)

links = soup.find_all('h2')

final_list = []
for item in links:
    link = item.find('a')
    final_list.append(link.get('href'))

minutes = input("Enter minute: ")
seconds = input("Enter seconds: ")

print("https://soundcloud.com" + final_list[0] + '#t=' + minutes + 'm' + seconds+ 's')

r2 = requests.get("https://soundcloud.com" + final_list[0] + '#t=' + minutes + 'm' + seconds+ 's')
test = re.findall(r'soundcloud.com/tracks/\d{3,9}', r2.text)

for item in test:
    print(item)









