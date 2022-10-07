import requests
import xml.etree.ElementTree as ET
import os
channels = {
    "dagbladet" : "https://www.dagbladet.no/?lab_viewport=rss",
    "vg" : "https://www.vg.no/rss/feed",
    "nrk" : "https://www.nrk.no/toppsaker.rss",
}

def parse(name, url):
    # url of rss feed

    # creating HTTP response object from given url
    resp = requests.get(url)

    file = f"{name}.xml"
    os.rename(file, "TEMP.xml")
    # saving the xml file
    with open(file, 'wb') as f:
        f.write(resp.content)
    #print(resp.content)
    def parseXML(xmlfile):
    
        # create element tree object
        tree = ET.parse(xmlfile)
    
        # get root element
        root = tree.getroot()
    
        # create empty list for news items
        newsitems = []
        olditems = []

        oldtree = ET.parse(file)
        oldroot = oldtree.getroot()

        for item in root.findall('./channel/item'):

            # empty news dictionary
            oldnews = {}

            # iterate child elements of item 

            for child in item:
                # special checking for namespace object content:media
                if child.tag == '{http://search.yahoo.com/mrss/}content':
                    oldnews['media'] = child.attrib['url']
                else:
                    oldnews[child.tag] = str(child.text).encode('utf8')

            # append news dictionary to news items list
            olditems.append(oldnews)
            #print(len(olditems), "old")
    
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
            #print(len(newsitems), "raw_new")
            #new_items = [x for x in newsitems if x not in olditems]
            #print(len(new_items), "new")
        # return news items list
        #print(newsitems[0])
        for x in newsitems:
            try:
                requests.post("http://127.0.0.1:8000/", data={'title': x["title"], "img" : x["media"], "link" : x["link"], 'channel': 1})
                print(x["title"])
            except:
                pass
            return newsitems
    parseXML(file)
    
while True:
    for x, y in channels.items():
        parse(x, y)