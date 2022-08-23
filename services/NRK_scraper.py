import requests
from bs4 import BeautifulSoup

NRK = "https://www.nrk.no/"

page = requests.get(NRK).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="kur-room__content")

def scrape():
    title_source = doc.find(class_="kur-room__content")
    title = str(title_source.span.contents[4])
    img_source = doc.find_all("img")
    img = str(img_source[0]).split()[38]
    article_source = doc.find_all("a")[45]
    article_link = article_source["href"]
    return title, img, article_link

title, img, article_link = scrape()

res = requests.post('http://127.0.0.1:8000/', data={'Title': title, "img": img, "link": article_link, "network": 1})