# Scrapping a particular website (Flipkart)
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone+15"
flipcart_url

flipcart_url1 = "https://www.flipkart.com/search?q=" + "tv"
flipcart_url1

urlclient = urlopen(flipcart_url1)
flipcart_page = urlclient.read()
flipcart_page

flipcart_html = bs(flipcart_page, "html.parser")
flipcart_html

"https//www.flipkart.com"+"https://rukminim2.flixcart.com/image/312/312/xif0q/television/x/8/a/-original-imagttjpuyzsbzud.jpeg?q=70"

big_box = flipcart_html.find_all("div",{"class":"_1AtVbE col-12-12"})
big_box
len(big_box) # For 30 products div class is same
del big_box[0:3]

productlink = "https://www.flipkart.com" + big_box[0].div.div.div.a['href']

for i in big_box:
    print("https://www.flipkart.com" + big_box[0].div.div.div.a['href'])
productlink

product_req = requests.get(productlink)
product_html = bs(product_req.text,'html.parser')
product_html

product_html.find_all("div",{"class":"_16PBlm"}) # comment class
comment_box = product_html.find_all("div",{"class":"_16PBlm"})
len(comment_box)  # Total 11 comments are there

comment_box[0].div.div.find_all("p",{"class":"_2sc7ZR _2V5EHH"})[0].text  # Name of the person who has commented
for i in comment_box:
    print(i.div.div.find_all("p",{"class":"_2sc7ZR _2V5EHH"})[0].text) # Fetching every customer names one by one  who commented on a product

# If you want to fetch ratings of every customer on a product
for i in comment_box:
    print(i.div.div.div.div.text)

# Fetching headers of the comments
comment_box[0].div.div.div.p.text
for i in comment_box:
    print(i.div.div.div.p.text )

# Fetching actual comments
comment_box[0].div.div.find_all("div",{"class":""})[0].text
for i in coment_box:
    print(i.div.div.find_all("div",{"class":""})[0].text)




    




