import requests
from bs4 import BeautifulSoup

def main(keyword, numberofitems):
    url = 'https://www.newegg.com/p/pl'
    query = keyword.replace(' ', '+')
    params = dict(d=query)

    r = requests.get(url, params= params)
    soup = BeautifulSoup(r.content, 'html.parser')
    items = soup.find_all('div', {'class': 'item-cell'}, limit = numberofitems)
    prices = []
    productlinks = []
    names = []
    productimages=[]
    newegglist=[]
    if len(items) > 0:
        for item in items:
            title = item.find('a', {'class': 'item-title'})
            names.append(title.getText())
            productlinks.append(title['href'])
            imageurl=item.find('a', {'class': 'item-img'})
            for i in imageurl:
                image = i['src']
            productimages.append(image)
            price = item.find('li', {'class': 'price-current'}).getText()
            p = price.replace(u'\xa0', u'')[:-1]
            price = p.split('(')[0]
            prices.append(price)
            newegglist.append([title.getText(),price, title['href'], image])
    return newegglist