import requests
import xml.etree.ElementTree as ET
import os

channels = {
    "dagbladet" : "https://www.dagbladet.no/?lab_viewport=rss",
    "vg" : "https://www.vg.no/rss/feed",
    "nrk" : "https://www.nrk.no/toppsaker.rss",
}

# lambda funksjon som sletter alle items i list1 som er i list2
match = lambda list1, list2: list(filter(lambda element: element not in list2, list1))

def create_file(name, url):
    pass
