# Django
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# tools
from comic_app.tools.extract_comic_titles import extract_image_comics
from comic_app.tools.generate_template import generate

#first party
import os
# Create your views here.

def index(request):
    comic_titles, comic_images = extract_image_comics()
    generate(comic_titles, comic_images)
    return render(request, "comic_app/new_template.html", None)
