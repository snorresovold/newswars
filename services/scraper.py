import requests
from bs4 import BeautifulSoup

VG = "https://www.vg.no/"

NRK = "https://www.nrk.no/"

page = requests.get(VG).text

doc = BeautifulSoup(page, "html.parser")

print(page)