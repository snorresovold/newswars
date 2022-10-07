import requests
import xml.etree.ElementTree as ET

channels = {
    "dagbladet" : "https://www.dagbladet.no/?lab_viewport=rss",
    "vg" : "https://www.vg.no/rss/feed",
    "nrk" : "https://www.nrk.no/toppsaker.rss",
}

def get_data(channel):
