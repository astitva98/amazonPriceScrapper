import requests
import bs4

URL = "https://www.amazon.in/Dell-Screen-LED-Lit-Monitor-P2419H/dp/B07F8XZN69/ref=sr_1_2?dchild=1&keywords=dell+p2419h&qid=1595792667&sr=8-2"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(URL , headers = headers)

soup = bs4.BeautifulSoup(page.text , 'lxml')

priceString = str(soup.find('span' , {"id" : "priceblock_ourprice"}))

lNum = priceString.find('>')

rNum = priceString[lNum : ].find('<')

price = priceString[lNum + 3: lNum+rNum]

print(price)

