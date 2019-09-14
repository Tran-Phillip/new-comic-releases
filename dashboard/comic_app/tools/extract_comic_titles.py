# first party
import re
import requests

# third party
from bs4 import BeautifulSoup

# tools
from comic_app.tools.extract_images import extract_images

def extract_image_comics():
    site = 'https://imagecomics.com/comics/new-releases'
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    comic_tags = soup.find_all(['img','span'])

    comics_and_images = []

    start_collecting = False # We don't want to collect everything. There is a lot of junk in the html
    for tag in comic_tags:
        if("Current" in str(tag)): # Current denotes when it will start listing the current comics for the image comics site
            start_collecting = True

        if(start_collecting): # assumption: the order will be img -> span -> img -> span
            if(tag.name == "img"):
                url = tag['src']
                comics_and_images.append(url)
            if(tag.name == "span"):
                result = re.search('<span>(.*)</span>', str(tag))
                try: # sometimes we dont find a match because the span has a tag
                    comics_and_images.append((result.group(1)))
                except:
                    pass
    comic_titles = comics_and_images[1:len(comics_and_images):2]
    comic_images = comics_and_images[0:len(comics_and_images):2]

    return comic_titles, comic_images
