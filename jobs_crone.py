from bs4 import BeautifulSoup
from pushbullet import Pushbullet
from requests import get
from googlesearch import search
from django.conf import settings


pushbullet_token = 'o.mdBqV1DwH5JanFJjl9NPt5FQD0REtZNG'
pb = Pushbullet(pushbullet_token)

ebook_url = 'https://ebookpoint.pl/'
audiobook_url = 'https://audiobooki.ebookpoint.pl/'

page = get(ebook_url)
content = BeautifulSoup(page.content, 'html.parser')

# get ebook in promotion
products = content.find(class_='promotion-book')

# remove prefix (/ksiazki/), remove additional text, reomve '-'
ebook = products.find('a', class_="bubble-title")[
    'href'].removeprefix('/ksiazki/').split(',')[0].replace('-', ' ')
ebook += ' lubimy czytac'
ebook_url = list(search(ebook, stop=1))[0]

# send link with ebook to phone
pb.push_link(title='ebook' ,url=ebook_url)

# ---------------------AUDIOBOOK-------------------------

audiobook_url = 'https://audiobooki.ebookpoint.pl/'
page = get(audiobook_url)
content = BeautifulSoup(page.content, 'html.parser')

# get audiobook in promotion
products = content.find(class_='promotion-book promotion-audiobook')

# remove prefix (/ksiazki/), remove additional text, reomve '-'
audiobook = products.find('a', class_="bubble-title")[
    'href'].removeprefix('/ksiazki/').split(',')[0].replace('-', ' ')
audiobook += ' lubimy czytac'
audiobook_url = list(search(audiobook, stop=1))[0]

# send link with audiobook to phone
pb.push_link(title='audiobook', url=audiobook_url)
