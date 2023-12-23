pip install webdriver_manager

1.from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService(r"C:\Users\shais\OneDrive\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")
import time
time.sleep(4)
driver.maximize_window()
time.sleep(5)

2.driver.title

3.r=driver.current_url
print(r)

4.import urllib.request
url="https://www.saucedemo.com/"
file=urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8").strip()
    print(decoded_line)