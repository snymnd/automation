from webdriver import driver
import pandas as pd

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


pd.DataFrame(result).to_csv("result.csv", index=False)