from bs4 import BeautifulSoup
import json
import requests

def parseProduct():
 pass

# get HTML
resp = requests.get("https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/n-bk7-plano-convex-lenses-ar-400-700nm-SLB-P-M.html")


soup = BeautifulSoup(resp.text, "html.parser")

# get only Rows, so we can only access to links
table = soup.find('tbody', {'class': "grouped-items-body"})

#get links (<a)
links = [link.get('href') for link in table.find_all('a')]

#dictionary
products_dict = {}

#debug purpose only:
link_count = 0

#treat every link
for link in links:
    link_count = link_count + 1
    print("Treating the " + str(link_count) + " link: "+ link)
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    table = soup.find('table', {'id': 'product-attribute-specs-table'})

    rows = [row for row in table.find_all('tr')]

    product = {}
    for row in rows:
       product[row.find('th', {'class':'col label'}).string] = row.find('td', {'class':'col data'}).string
    
    code = soup.find('div', {'class': 'product-info-sku'})

    products_dict[code.p.span.string] = product


with open("product.json", "w") as json_file:
    json.dump(products_dict, json_file, indent=4)

# print the HTML as text
print("Done! Check the json file!")