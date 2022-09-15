from selenium import webdriver
#from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get("https://tte.kominfo.go.id/verifyPDF")
    element = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(element)
    upload_button = driver.find_element_by_tag_name("input")
    upload_button.send_keys("D:/Downloads/tes.pdf")
except:
    driver.close()