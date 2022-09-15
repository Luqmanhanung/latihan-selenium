from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")
print(driver.title)
driver.close()