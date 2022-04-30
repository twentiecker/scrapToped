from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

url = "https://www.tokopedia.com/p?nref=chead"
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(f"{url}")
time.sleep(2)  # Allow 2 seconds for the web page to open
page_soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

# Get content category
content_soup = page_soup.find_all("div", {"class": "getScrollPosition css-1gi0ami"})
print(len(content_soup))

# Scraping category by level
list_category = []
for x in content_soup:
    level1 = x.find("div", {"class": "css-79elbk e13h6i9f0"})  # Buku
    print(level1.text)
    list_category.append(level1.text)
    level2 = x.find("div", {"class": "css-1g1liea"})
    y = level2.find_all("div", {"class": "css-cdv2tj e13h6i9f2"})
    for z in y:
        # print(z.text)
        category = z.find_all("a", {"class": "css-15sd2h4"})
        for a in category:
            print(f";{a.text}")
            list_category.append(f";{a.text}")
            sub_category_soup = z.find_all("a")
            for b in sub_category_soup:
                if b.text == a.text:
                    continue
                else:
                    print(f";;{b.text}")
                    list_category.append(f";;{b.text}")
# print(len(list_category))

# Write scraped data to a csv file (semicolon separated)
f = open(f"toped_direktori.csv", "w+", encoding="utf-8")  # open/create file and then append some item (a+)
headers = "Level 1;Level 2;Level 3\n"
f.write(headers)
for i in range(len(list_category)):
    f.write(f"{list_category[i]}\n")
f.close()