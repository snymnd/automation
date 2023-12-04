from webdriver import driver
import pandas as pd
from datetime import datetime
import os
import sys

date = datetime.now()
str_now = date.strftime("%Y-%m-%d")

application_path = os.path.dirname(sys.executable)

containers = driver.find_elements(
    by="xpath", value='//*[@id="user-repositories-list"]/ul/li'
)

result = {"title": [], "link": []}

for container in containers:
    title = container.find_element("xpath", value="./div[1]/div[1]/h3/a").text
    link = container.find_element("xpath", value="./div[1]/div[1]/h3/a").get_attribute(
        "href"
    )
    result["title"].append(title)
    result["link"].append(link)

file_name = f"result_{str_now}.csv"
res_path = os.path.join(application_path, file_name)

pd.DataFrame(result).to_csv(res_path)

driver.quit()

## run with pyinstaller to make an executable (py to exe)
#  pyinstaller --onefile repo_listing.py
## then the executable will be in dist folder