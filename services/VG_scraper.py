import requests
from bs4 import BeautifulSoup
import os

VG = "https://www.vg.no/"

page = requests.get(VG).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="article")

def scrape():
    title = page_text.span.contents
    try:
        img = page_text.img["src"]
    except TypeError:
        print("could not get image")
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/VG_logo.svg/300px-VG_logo.svg.png?20150226094714"
    article_link = page_text.a["href"]
    return title, img, article_link

def webpage_was_changed(): 
    """Returns true if the webpage was changed, otherwise false."""

    response = doc.find(class_="article")
    article_link = response.a["href"]

    # create the previous_content.txt if it doesn't exist
    if not os.path.exists("previous_content.txt"):
        open("previous_content.txt", 'w+').close()

    filehandle = open("previous_content.txt", 'r')
    previous_response_html = filehandle.read() 
    filehandle.close()

    if previous_response_html == article_link:
        print(article_link)
        return False
    else:
        filehandle = open("previous_content.txt", 'w')
        filehandle.write(article_link)
        filehandle.close()
        return True

# Upload send data to api
i = 1
while True:
    print(i)
    i+=1
    if webpage_was_changed() == False:
        print("nothing has changed")
    else:
        title, img, article_link = scrape()
        res = requests.post('http://127.0.0.1:8000', data={'title': title, "img": img, "link": article_link, "channel": 1})
        print(res)