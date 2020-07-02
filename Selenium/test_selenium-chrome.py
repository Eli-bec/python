'''
Using Chrome driver
This was test333.py
'''

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

for i in range (1,20):
    symbol='0'*(4-len(str(i)))+str(i)+'.HK'
    driver.get('https://hk.finance.yahoo.com/quote/'+symbol)
    soup = BeautifulSoup(driver.page_source,"lxml")
    try: item = soup.find(id="quote-market-notice").find_parent().find("span").text
    except: item=''
    print(i,item)

driver.quit()
