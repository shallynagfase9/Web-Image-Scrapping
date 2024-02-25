import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
import os
sav_dir = "images/"
if not os.path.exists(sav_dir):
    os.makedirs(sav_dir)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
query = "elon musk"
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")
response
response._content

soup = bs(response.content,"html.parser")
image_tags = soup.find_all('img')
del image_tags[0]
image_tags

len(image_tags)
image_data_mongo = []
for i in image_tags:
    image_url =  i['src']
    image_data = requests.get(image_url).content
    mydict = {"index" : image_url , "image" : image_data}
    image_data_mongo.append(mydict)
    with open(os.path.join(sav_dir,f"{query}_{image_tags.index(i)}.jpg") , "wb") as f :
                           f.write(image_data)





