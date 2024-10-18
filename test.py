from bs4 import BeautifulSoup
from product import Product
import json
import requests

# get HTML
resp = requests.get("https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/n-bk7-plano-convex-lenses-ar-400-700nm-SLB-P-M.html")

html = resp.text

soup = BeautifulSoup(html, "html.parser")

# get only Rows, so we can only access to links
table = soup.find('tbody', {'class': "grouped-items-body"})

#get links (<a)
links = [link.get('href') for link in table.find_all('a')]

# print the HTML as text
print(links)