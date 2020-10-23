import requests
import api

url = "https://rapidapi.p.rapidapi.com/search.php"
def main(keyword, numberofitems):
    querystring = {"query": keyword, "page":"1"}
    headers = {
    'x-rapidapi-host': "walmart-search.p.rapidapi.com",
    'x-rapidapi-key': api.walmartkey
    }
    walmartlist=[]
    r = requests.request('GET', url, headers= headers, params=querystring)
    for item in r.json()['items']:
        title=item['title']
        price=item['price']
        link= f"https://www.walmart.com/ip/{item['id']}"
        imagelink = item['image']
        walmartlist.append([title, price, link, imagelink])
    return walmartlist[0:9]
