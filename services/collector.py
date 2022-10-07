import requests
import xml.etree.ElementTree as ET

channels = {
    "dagbladet" : "https://www.dagbladet.no/?lab_viewport=rss",
    "vg" : "https://www.vg.no/rss/feed",
    "nrk" : "https://www.nrk.no/toppsaker.rss",
}

def convert(name, url):
    file = f"{name}.xml"
    resp = requests.get(url)
    return file, resp.content

def parse(input):
    # create element tree object
    tree = ET.parse(input)
    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel/item'):

        # empty news dictionary
        news = {}

        # iterate child elements of item 

        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = str(child.text).encode('utf8')

        # append news dictionary to news items list
        newsitems.append(news)
    return newsitems

def match(name, url):
    con_name, con_url = convert(name, url)
    name_data = parse(con_name)
    url_data = parse(con_url)
    curated_list = [x for x in url_data if x not in name_data]
    with open(con_name, 'wb') as f:
        f.write(url_data)
    return curated_list

for name, url in channels.items():
    match(name, url)