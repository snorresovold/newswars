import requests
from bs4 import BeautifulSoup

VG = "https://www.vg.no/"

page = requests.get(VG).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="article")

def scrape():
    title = page_text.span.contents
    img = page_text.img["src"]
    article_link = page_text.a["href"]
    return title, img, article_link

title, img, article_link = scrape()
#print(title, img, article_link)

# Upload send data to api
res = requests.post('http://127.0.0.1:8000', data={'Title': title, "img": img, "link": article_link, "network": 1})
#print(res)