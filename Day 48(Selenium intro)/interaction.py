from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://en.wikipedia.org/wiki/Main_Page"


def main():

    # Keep the browser op after program finishes
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option('detach', True)

    browser = webdriver.Edge(options=edge_options)
    browser.get(url=URL)

    articlecount = browser.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

    #[print(event.text) for event in event_list]
    print(articlecount.text)

    # Close closes a single tab and quit shuts down the browser
    # browser.close()
    browser.quit()


if __name__ == '__main__':
    main()
