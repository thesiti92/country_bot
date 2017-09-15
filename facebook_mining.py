from bs4 import BeautifulSoup
import json
from datetime import datetime

soup = BeautifulSoup(open("messages.html", encoding="utf8"), 'lxml').body.contents[1]

json.dump(open("messages.json", 'w+'), [{'user': message.contents[0].get('div', class_="user").text, 'date': datetime(message.contents[0].get('div', class_="meta").text), 'message': message.next_sibling} for thread_set in soup.contents for thread in thread_set for message in thread.find_all('div') ])
