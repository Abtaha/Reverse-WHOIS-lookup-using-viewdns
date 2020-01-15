from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def getData(browser, input):
    browser.get(f"https://viewdns.info/reversewhois/?q={input}")
    
    rows = browser.find_elements_by_tag_name("tr")
    data = []
    for row in rows:
        data.append(row.find_elements_by_tag_name("td"))
    
    return data

opts = Options()
opts.headless = True
opts.add_argument('log-level=2')
assert opts.headless
browser = Chrome(options=opts)

inp = input("Enter the Registrant Name or Email Address >> ")
data = getData(browser, inp)

for i in data:
    for x in i:
        if x:
            print(f"{x.text}", sep="    ")
    print()

browser.close()