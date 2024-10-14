from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = "https://orteil.dashnet.org/experiments/cookie/"

global browser
global cookie_button, cursor_button, grandma_button, factory_button, mine_button, shipment_button, alchlab_button, portal_button, time_machine_button
global cursor_cost, grandma_cost, factory_cost, mine_cost, shipment_cost, alchlab_cost, portal_cost, time_machine_cost


def get_browser():
    global browser
    # Keep the browser op after program finishes
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)

    # get the webpage from URL
    browser = webdriver.Edge(options=edge_options)
    browser.get(url=URL)


def get_elements():
    global browser
    global cookie_button, cursor_button, grandma_button, factory_button, mine_button, shipment_button, alchlab_button, portal_button, time_machine_button

    # get the buttons
    cookie_button = browser.find_element(By.ID, value='cookie')
    cursor_button = browser.find_element(By.ID, value='buyCursor')
    grandma_button = browser.find_element(By.ID, value='buyGrandma')
    factory_button = browser.find_element(By.ID, value='buyFactory')
    mine_button = browser.find_element(By.ID, value='buyMine')
    shipment_button = browser.find_element(By.ID, value='buyShipment')
    alchlab_button = browser.find_element(By.ID, value='buyAlchemy lab')
    portal_button = browser.find_element(By.ID, value='buyPortal')
    time_machine_button = browser.find_element(By.ID, value='buyTime machine')
    cursor_button = browser.find_element(By.ID, value='buyCursor')


def upgrade_cost():
    global browser

    global cursor_cost, grandma_cost, factory_cost, mine_cost, shipment_cost, alchlab_cost, portal_cost, time_machine_cost

    # get the upgrade costs

    cost = browser.find_element(
        By.CSS_SELECTOR, value='#buyCursor b').text
    cursor_cost = cost.split()[2]

    cost = browser.find_element(
        By.CSS_SELECTOR, value='#buyGrandma b').text
    grandma_cost = cost.split()[2]

    cost = browser.find_element(
        By.CSS_SELECTOR, value='#buyFactory b').text
    factory_cost = cost.split()[2]

    cost = browser.find_element(
        By.CSS_SELECTOR, value='#buyMine b').text
    mine_cost = cost.split()[2]

    cost = browser.find_element(
        By.CSS_SELECTOR, value='#buyShipment b').text
    shipment_cost = cost.split()[2]

    cost = browser.find_element(
        By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text
    alchlab_cost = cost.split()[2]
    print(alchlab_cost)
    cost = browser.find_element(
        By.CSS_SELECTOR, value='#buyPortal b').text
    portal_cost = cost.split()[2]

    cost = browser.find_element(
        By.XPATH, value='//*[@id="buyTime machine"]/b').text
    time_machine_cost = cost.split()[2]

def cookies_clicked():
    global browser

    return browser.find_element(By.ID, value='money').text
    

def main():
    global browser, cursor_button, cursor_cost, cookie_button
    
    get_browser()
    get_elements()
    upgrade_cost()

    while True:
        for clicks in range(0,12):
            cookie_button.click()
        
        upgrade_cost()
        print(cursor_cost)
        print(cookies_clicked())
        sleep(2)

    browser.quit()


if __name__ == '__main__':
    main()
