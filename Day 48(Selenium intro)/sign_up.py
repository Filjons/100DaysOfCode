from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "https://secure-retreat-92358.herokuapp.com/"
FIRST_NAME = 'Filip'
LAST_NAME = 'Jonsson'
EMAIL = 'fijji88@gmail.com'


def main():

    # Keep the browser op after program finishes
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)

    # get the webpage from URL
    browser = webdriver.Edge(options=edge_options)
    browser.get(url=URL)

    # get the wanted elements
    name = browser.find_element(By.NAME, value=F'fName')
    sure_name = browser.find_element(By.NAME, value='lName')
    email = browser.find_element(By.NAME, value='email')
    button = browser.find_element(By.CSS_SELECTOR, value='form button')

    # fill out the text form and submit your soul
    name.send_keys(FIRST_NAME)
    sure_name.send_keys(LAST_NAME)
    email.send_keys(EMAIL)
    button.click()

    # browser.quit()


if __name__ == '__main__':
    main()
