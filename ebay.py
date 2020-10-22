import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import api
def main(keyword, numberofitems):
    url='https://svcs.ebay.com/services/search/FindingService/v1'
    appid = api.ebaykey
    params = {'SECURITY-APPNAME': appid,'OPERATION-NAME':'findItemsByKeywords','keywords': keyword, 'paginationInput.entriesPerPage': numberofitems}
    r = requests.get(url, params = params)

    links=[]
    names=[]
    prices=[]
    imageurls=[]
    ebaylist = []

 
    r_body_xml = ET.fromstring(r.content)
    tree = ET.ElementTree(r_body_xml)
    root = tree.getroot()
    
    for item in root.find('{http://www.ebay.com/marketplace/search/v1/services}searchResult'):
        link = item.find('{http://www.ebay.com/marketplace/search/v1/services}viewItemURL').text
        links.append(link)
        name = item.find('{http://www.ebay.com/marketplace/search/v1/services}title').text
        names.append(name)
        sellingStatus = item.find('{http://www.ebay.com/marketplace/search/v1/services}sellingStatus')
        price = sellingStatus.find('{http://www.ebay.com/marketplace/search/v1/services}currentPrice').text
        prices.append(price)
        iurl = item.find('{http://www.ebay.com/marketplace/search/v1/services}galleryURL').text
        imageurls.append(iurl)
        ebaylist.append([name, price, link, iurl])

    return ebaylist
    



