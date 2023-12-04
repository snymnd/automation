from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

## Headless mode, making the browser invisible (run in background)
options.add_argument("--headless=new")   


website = "https://github.com/snymnd?tab=repositories"
# adjust your file directory here
webdriver_path = "/home/snymnd/project/Automate/chromedriver"
print(webdriver_path)

service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)
