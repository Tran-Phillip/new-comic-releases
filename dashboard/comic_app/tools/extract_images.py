# first party
import re
import requests

# third party
from bs4 import BeautifulSoup
import os
def extract_images(url:str):
    '''
    Uses beautiful soup to extract an image from a webpage.
    Ideally url should be a link to the image extracted from "main.py"

    :param url: python string representing the url to extract the images from
    :return: This function returns 0 if the operation was successful and downloads
             the image to a temp folder called 'images', which will be deleted
             at the end of program execution to prevent cluttering.
             Returns 1 if the program failed to execute.
    '''

    # Source: https://stackoverflow.com/questions/18408307/how-to-extract-and-download-all-images-from-a-website-using-beautifulsoup
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|jpeg))$', url) # potential smell here. If a new image format is added, make sure to include it here
    with open("comic_app/static/comic_app/images/"+str(filename.group(1)), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative
            # if it is provide the base url which also happens
            # to be the site variable atm.
            url = '{}{}'.format("image_", url)
        response = requests.get(url)
        f.write(response.content)
    return(str(filename.group(1)))
