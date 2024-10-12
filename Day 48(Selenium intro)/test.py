from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.amazon.com/dp/B08CFZF16Y/ref=sbl_dpx_kitchen-electric-cookware_B0CXY2QJ4G_0"


''' Useful functions in Selenium
    search_bar = browser.find_element(By.name, value="q")
    print8)

'''






def main():
  
    # Keep the browser op after program finishes
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)

    browser = webdriver.Edge(options=edge_options)
    browser.get(url=URL)

    price_whole = browser.find_element(By.CLASS_NAME, value='a-price-whole')
    price_fraction = browser.find_element(By.CLASS_NAME, value='a-price-fraction')

    print(f'The price is {price_whole.text}.{price_fraction.text}')
    # Close closes a single tab and quit shuts down the browser
    # browser.close()
    browser.quit()


if __name__ == '__main__':
    main()
