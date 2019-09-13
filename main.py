# first party
import re
import requests
import os

# third party
from bs4 import BeautifulSoup
from flask import Flask, render_template

# tools 
from tools.extract_images import extract_images

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join("images")
@app.route('/')
def foo():
    try:
        os.mkdir("images")
    except: 
        pass
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

    name = extract_images(comics_and_images[0])
    print("images/"+name)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], name)
    return render_template('index.html', user_image = "/home/jiksa/Documents/projects/comic_app/images/"+name) 






# print(soup.prettify())
# comic_tags = soup.find_all('a') 
# for tag in comic_tags: # go through each tag and try to parse it by it's href
#     try:
#         print(tag['href'])
#     except:
#         pass
# print(comics)
