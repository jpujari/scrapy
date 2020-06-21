from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
from bs4 import BeautifulSoup
from flask import Flask

def getResults():
  from selenium import webdriver
  url = 'https://www.myntra.com/men-briefs-and-trunks'
  chrome_driver_path = '/usr/local/bin/chromedriver'
  agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument(f'user-agent={agent}')
  webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
  )

  with webdriver as driver:
      # Set timeout time
      wait = WebDriverWait(driver, 10)
      # retrive url in headless browser
      driver.get(url)
      product_table_data = []
      column_names = ['Brand', 'Product', 'Price', 'Discount Price']
      product_table_data.append(column_names)
      content = driver.page_source
      soup = BeautifulSoup(content, "html.parser")
      divs = soup.find_all("div",attrs={'class':'product-productMetaInfo'})
      for div in divs:
        brand = div.find('h3', attrs={'class':'product-brand'})
        product = div.find('h4', attrs={'class':'product-product'})
        price = div.find('span', attrs={'class': 'product-strike'})
        discountprice = div.find('span', attrs={'class': 'product-discountedPrice'})
        productpricediv = div.find('div', attrs={'class': 'product-price'})
        productprice = productpricediv.find('span')
        if brand:
            brandtext = brand.text
        else:
            brandtext = "No brand name"
        if product:
            producttext = product.text
        else:
            producttext = "No product name"
        if price:
            pricetext = price.text
        else:
            pricetext = "No price"
        if discountprice:
            discountpricetext = discountprice.text
        else:
            pricetext = productprice.text
            discountpricetext = "No discount price"
        # print(pricetext)
        row = [brandtext, producttext, pricetext, discountpricetext]
        product_table_data.append(row)

      from tabulate import tabulate
      tabledata = tabulate(product_table_data, tablefmt='html')
      driver.close()
  return tabledata

app = Flask(__name__)
@app.route("/")
def index():
  htmlcode = getResults()
  return htmlcode

# getResults()
#run this on command line
# env FLASK_APP=scrapy.py flask run