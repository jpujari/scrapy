from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from flask import Flask
from flask import send_file

def getResults():
  from selenium import webdriver
  url = 'https://www.myntra.com/men-briefs-and-trunks'
  chrome_driver_path = '/usr/local/bin/chromedriver'
  agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument(f'user-agent={agent}')
  chrome_options.add_argument("--no-sandbox");
  chrome_options.add_argument("--disable-dev-shm-usage");
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

      driver.close()
  return product_table_data

def getHtml():
    product_table_data = getResults()
    from tabulate import tabulate
    tabledata = tabulate(product_table_data, tablefmt='html')
    return tabledata

app = Flask(__name__)
@app.route("/")
def index():
  htmlcode = getHtml()
  return htmlcode

@app.route('/csv')
def csv():
    product_table_data = getResults()
    import csv
    with open("/tmp/data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(product_table_data)
    path = "/tmp/data.csv"
    return send_file(path, as_attachment=True)

# getResults()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')