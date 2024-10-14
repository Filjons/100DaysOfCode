from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.amazon.com/dp/B08CFZF16Y/ref=sbl_dpx_kitchen-electric-cookware_B0CXY2QJ4G_0"

# Useful functions in Selenium
'''
search_bar = browser.find_element(By.name, value="q")
print(search_bar.get_attribute("placeholder"))
button = browser.find_element(By.ID, value='submit')    
print(button.size)
document_link = browser.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(document_link.text)
'''
'''
bug_link = browser.find_element(By.XPATH, value= 'xpath from elemtn on page')
print(bug_link.text)
'''
'''
There is always a plural version of all the find functions in selenium
'''


def main():

    # Keep the browser op after program finishes
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)

    browser = webdriver.Edge(options=edge_options)
    browser.get(url=URL)

    price_whole = browser.find_element(By.CLASS_NAME, value='a-price-whole')
    price_fraction = browser.find_element(
        By.CLASS_NAME, value='a-price-fraction')

    print(f'The price is {price_whole.text}.{price_fraction.text}')
    # Close closes a single tab and quit shuts down the browser
    # browser.close()
    browser.quit()

if __name__ == '__main__':
    main()
