from selenium import webdriver

#Keep the browser op after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=edge_options)
driver.get('https://www.amazon.com')



