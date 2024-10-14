import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
HOUSING_URL = 'https://appbrewery.github.io/Zillow-Clone/'

housing_list = []
housing = {'price':'','size':'','address':''}

//*[@id = "zpid_2056905294"]/div/div[1]/a/address
def get_housing():
        
    # get all data from the web page

    responese = requests.get(HOUSING_URL)

    # parse the data into a soup using the html.parser
    soup = BeautifulSoup(responese.text, "html.parser")

    housing_price = soup.find(
        name="span", class_="PropertyCardWrapper__StyledPriceLine",)


    housing_size = soup.find(
    name="span", class_="StyledPropertyCardHomeDetailsList",)
    housing_address = soup.find(
    name="address", class_="PropertyCardWrapper__StyledPriceLine",)
    article_text = housing_list.get_text()

    print(article_text)


def main():
    get_housing()
    # Keep the browser op after program finishes
    '''
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)

    browser = webdriver.Edge(options=edge_options)
    browser.get(url=HOUSING_URL)

    price_whole = browser.find_element(By.CLASS_NAME, value='a-price-whole')
    price_fraction = browser.find_element(
        By.CLASS_NAME, value='a-price-fraction')

    print(f'The price is {price_whole.text}.{price_fraction.text}')
    '''
    # Close closes a single tab and quit shuts down the browser
    # browser.close()
    browser.quit()


if __name__ == '__main__':
    main()
