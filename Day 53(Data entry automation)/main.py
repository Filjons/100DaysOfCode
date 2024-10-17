import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import pprint


GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScUDSXwaj0e75DQSg155CCAQUAzYawWr_UMkkM5MGcfy1aHIQ/viewform?usp=sf_link'
HOUSING_URL = 'https://appbrewery.github.io/Zillow-Clone/'


housing_det = {'price': '', 'link': '', 'address': ''}
housing_list = []


def get_housing():

    # get all data from the web page

    responese = requests.get(HOUSING_URL).text

    # parse the data into a soup using the html.parser
    soup = BeautifulSoup(responese, 'html.parser')
    
    #print(soup.prettify())

    housings = soup.find_all('li', class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
    
    for n in housings:
        
        housing_det['price'] = n.find(class_="PropertyCardWrapper__StyledPriceLine",).get_text().strip()

        housing_det['address'] = n.find(name="address",).get_text().strip()
       
        housing_det['link'] = n.find(name="a", class_="StyledPropertyCardDataArea-anchor",).get('href')
        
        housing_list.append(housing_det)

    return housing_list


def main():
    housing = get_housing()
    # Keep the browser op after program finishes
    
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)1

    browser = webdriver.Edge(options=edge_options)
    browser.get(url=HOUSING_URL)

    price_whole = browser.find_element(By.CLASS_NAME, value='a-price-whole')
    price_fraction = browser.find_element(
        By.CLASS_NAME, value='a-price-fraction')

    print(f'The price is {price_whole.text}.{price_fraction.text}')
    
    # Close closes a single tab and quit shuts down the browser
    # browser.close()
    # browser.quit()


if __name__ == '__main__':
    main()
