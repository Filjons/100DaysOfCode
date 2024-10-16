import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
HOUSING_URL = 'https://appbrewery.github.io/Zillow-Clone/'

housing_list = []
housing_det = {'price': '', 'size': '', 'address': ''}


def get_housing():

    # get all data from the web page

    responese = requests.get(HOUSING_URL)

    # parse the data into a soup using the html.parser
    soup = BeautifulSoup(responese.text, "html.parser")
    housings = soup.find(name='ul')
    for n in range(0,5):
        housing = housings.find_next(
            name='li', class_="ListItem-c11n-8-84-3-StyledListCardWrapper",)
        
        housing_address = housing.find(name = "address",)

        housing_det['address'] = housing_address.get_text().strip()
     

        print(housing_det)


def main():
    get_housing()
    # Keep the browser op after program finishes
    '''
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)1

    browser = webdriver.Edge(options=edge_options)
    browser.get(url=HOUSING_URL)

    price_whole = browser.find_element(By.CLASS_NAME, value='a-price-whole')
    price_fraction = browser.find_element(
        By.CLASS_NAME, value='a-price-fraction')

    print(f'The price is {price_whole.text}.{price_fraction.text}')
    '''
    # Close closes a single tab and quit shuts down the browser
    # browser.close()
    # browser.quit()


if __name__ == '__main__':
    main()
