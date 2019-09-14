# Django
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# tools
from comic_app.tools.extract_comic_titles import extract_image_comics
from comic_app.tools.extract_comic_titles import extract_marvel_comics
from comic_app.tools.generate_template import generate

#first party
import os
# Create your views here.

def index(request):
    image_comic_titles, image_comic_images = extract_image_comics()
    marvel_comic_titles, marvel_comic_images = extract_marvel_comics()

    comic_titles = image_comic_titles + marvel_comic_titles
    comic_images = image_comic_images + marvel_comic_images
    generate(comic_titles, comic_images)
    return render(request, "comic_app/dashboard.html", None)
