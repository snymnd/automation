from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os

os_path = os.path.dirname(os.path.realpath(__file__))

website = "https://github.com/snymnd?tab=repositories"
webdriver_path = os_path + "/chromedriver"

service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service)

driver.get(website)
