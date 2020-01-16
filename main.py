# Import libraries
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup as soup


try:
    inp = input("Enter the name of the organization >> ")
    req = Request(f'https://viewdns.info/reversewhois/?q={inp}', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = soup(webpage, "html.parser")
    rows = soup.findAll("table")[3].findAll("tr")#.findAll("rows")


    for row in rows:
        for cell in row:
            print(cell.text, sep="      ")
        print()
except:
    print("Error")