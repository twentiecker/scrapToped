from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

url = "https://www.tokopedia.com/daftar-halaman/"
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(f"{url}")
time.sleep(2)  # Allow 2 seconds for the web page to open
page_soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

# Get content category
content_soup = page_soup.find_all("div", {"class": "css-1c5ij41"})
print(len(content_soup))

# Scraping category by level
list_category = []
for x in content_soup:
    level1_tag = x.find_all("a", {"class": "css-1m9lpdg"})
    for y in level1_tag:
        print(y.text)
        list_category.append(y.text)
        level2_tag = x.find_all("a", {"class":"css-1ehjfos"})
        for z in level2_tag:
            print(f";{z.text}")
            list_category.append(f";{z.text}")

# Write scraped data to a csv file (semicolon separated)
f = open(f"toped_daftar_halaman.csv", "w+", encoding="utf-8")  # open/create file and then append some item (a+)
headers = "Level 1;Level 2\n"
f.write(headers)
for i in range(len(list_category)):
    f.write(f"{list_category[i]}\n")
f.close()
