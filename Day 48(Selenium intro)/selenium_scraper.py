from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://www.python.org/events/"


def main():

    # Keep the browser op after program finishes
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)

    browser = webdriver.Edge(options=edge_options)
    browser.get(url=URL)

    event_list = browser.find_elements(By.CSS_SELECTOR, value=".event-title")

    [print(event.text) for event in event_list]
    #print(event_list)

    # Close closes a single tab and quit shuts down the browser
    # browser.close()
    browser.quit()

if __name__ == '__main__':
    main()
