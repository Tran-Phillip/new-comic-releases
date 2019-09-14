
def generate(list_of_comics_titles:list, list_of_comics_images:list):
    '''
    generates a html template and includes as many image and span
    tags as are gotten from the extract_comic_titles function

    :param list_of_comics_titles: python list representing all the comics collected from 'extract_comic_titles'
    :param list_of_comics_images: python list representing all the comic images collected from 'extract_comic_titles'
    :return nothing, but generates the html template in templates/comic_app
    '''

    with open("comic_app/templates/comic_app/new_template.html", 'w') as f:
        f.write('<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">\n')
        f.write("{% load static %}\n")
        f.write('\n<link rel="stylesheet" type="text/css" href="{% static \'comic_app/style.css\' %}">\n')
        f.write("<html>\n")
        f.write("<body>\n")
        f.write('<main class="wrapper">\n')
        f.write('<div class="row">\n')
        for comic,image in zip(list_of_comics_titles, list_of_comics_images):
            f.write('<div class="column">\n')
            f.write("<img src="+image+" alt class=\"u-mb0_5 block with-border\">\n")
            f.write("   <span class=\"title\">\n")
            f.write("    " + comic)
            f.write("\n    </span>\n")
            f.write("\n</div>\n")
        f.write("</div>\n")

        f.write("</body>\n")
        f.write("</html>\n")
