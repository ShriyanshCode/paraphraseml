from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
#python -m venv venv
#.\venv\Scripts\activate

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://webscraper.io/test-sites/e-commerce/allinone")
print(driver.title)

wait = WebDriverWait(driver, 10)
computers_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/test-sites/e-commerce/allinone/computers')]")))
computers_link.click()


laptop_link = driver.find_element(By.XPATH,"//a[contains(@href, '/test-sites/e-commerce/allinone/computers/laptops')]")
laptop_link.click()
print(driver.title)
time.sleep(2)

titles=[]
desc=[]
reviews=[]

desc_ele = driver.find_elements(By.XPATH, "//p[@class='description card-text']")
for des in desc_ele:
    desc.append(des.text)

div_elements = driver.find_elements(By.XPATH, "//div[@class='caption']")
for div_element in div_elements:
    h4_element = div_element.find_element(By.XPATH, ".//h4/a[@class='title']")
    titles.append(h4_element.text)

atr=driver.find_elements(By.XPATH,"//p[@class='float-end review-count']")
 
for des in atr:
    reviews.append(des.text)


titles2 = [0 if item is None or item == '' else item.replace('...', '') for item in titles]
list1 = [0 if not x else x for x in titles2]
list2 = [0 if not x else x for x in desc]
list3 = [0 if not x else x for x in reviews]



extralinks=[]
b1=[]
b3=[]
extras=driver.find_elements(By.XPATH,"//ul//li")

for li in extras:
    a_elements = li.find_elements(By.TAG_NAME, 'a')
    for a in a_elements:
        href = a.get_attribute("href")
        extralinks.append(href)
        b1.append(a.text)
li_elements = driver.find_elements(By.XPATH, "//ul//li")
for li in li_elements:
    b3.append(li.text)
    
temp3 = []
for element in b1:
    if element not in b3:
        b3.append(element)
extraelements = ['Non-Clickable Element' if item == '' else item for item in b3]

mydic={'ProductName':list1,
       'ProductDesc':list2,
       'ProductReview':list3,
       'ExtraLinks':extralinks,
       'ExtraTextCSS':extraelements}
driver.quit()
