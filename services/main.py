import requests
import xml.etree.ElementTree as ET
import time

channels = {
    "vg" : "https://www.vg.no/rss/feed",
    "nrk" : "https://www.nrk.no/toppsaker.rss",
    "tv2" : "https://www.tv2.no/rest/cms-feeds-dw-rest/v2/cms/article/nyheter",
    "dagavisen" : "https://www.dagsavisen.no/arc/outboundfeeds/rss/"
}

# lambda funksjon som sletter alle items i list1 som er i list2
match = lambda list1, list2: list(filter(lambda element: element not in list2, list1))

# converts a string to the name of an xml file
convert = lambda input : f"{input}.xml"

print(convert("dagbladet"))

def create_file(name, url):
    # url of rss feed
    # creating HTTP response object from given url
    resp = requests.get(url)

    file = convert(name)
    # saving the xml file
    with open(file, 'wb') as f:
        f.write(resp.content)
    
    return file

file = create_file("dagbladet", "https://www.dagbladet.no/?lab_viewport=rss")

def parse_file(file):
    # create element tree object
    tree = ET.parse(file)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []
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



while True:
    id = 0
    for x, y in channels.items():
        id += 1 
        print(f"id of {x} is {id}")
        old_list = parse_file(convert(x))
        # get scrape new items
        create_file(x, y)
        # store them
        new_list = parse_file(convert(x))

        # curate
        curated_list = match(new_list, old_list)
        
        print(curated_list)
        if len(curated_list) != 0:
            for i in curated_list:
                print("sleeping 1 second")
                time.sleep(1) # hopeful error fix
                requests.post("http://127.0.0.1:8000/", data={'title': i["title"], "link" : i["link"], 'channel': id})
        else:
            print("curated list is empty")


        # we need to create a new file at the end so we can use it for the next old_list
        create_file(x, y)
        time.sleep(1)
        print("sleeping \n")
