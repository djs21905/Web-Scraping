import requests
from bs4 import BeautifulSoup

# User input for artist name/ song name
search_query = input("Enter search query: ")

# Creates an http req and retrieves the url based on the artist/ song name
r = requests.get("https://www.youtube.com/results?search_query=" + search_query)

# Converts the html request object to a soup object
soup = BeautifulSoup(r.text)

# Finds all instances of a div with a specific class --> appends each instance to a list
links = soup.find_all('div', {"class": "yt-lockup-content"})

# Iterates through the list , finds the links and appends them to to final_list
final_list = []
for item in links:
    link = item.find('a')
    final_list.append(link.get('href'))

# Removes all links containing string channel or user
for index, item in enumerate(final_list):
    if "channel" in item:
        del final_list[index]
    elif "user" in item:
        del final_list[index]

print("https://www.youtube.com" + final_list[0])





