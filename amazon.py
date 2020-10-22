import requests
import api

url = "https://rapidapi.p.rapidapi.com/search"

def main(keyword, numberofitems):
    querystring = {"keywords":keyword,"marketplace":"US","page":"2"}
    headers = {
        'x-rapidapi-host': "amazon-price1.p.rapidapi.com",
        'x-rapidapi-key': api.amazonkey
    }
    r = requests.request("GET", url, headers= headers, params = querystring)
    info = r.json()
    prices = []
    productlinks = []
    names = []
    productimages=[]
    amazonlist=[]

    for i in range(numberofitems):
        try:
            item = info[i]
            name = item['title']
            price = item['price']
            link = item['detailPageURL']
            imglink = item['imageUrl']
            prices.append(price)
            names.append(name)
            productlinks.append(link)
            productimages.append(imglink)
            amazonlist.append([name, price, link, imglink])
        except:
            pass

    return amazonlist
