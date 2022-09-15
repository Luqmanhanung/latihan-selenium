from selenium import webdriver
#from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://verifikasipdf.rootca.or.id/")
element = driver.find_element_by_tag_name("input")
element.send_keys("D:/Downloads/tes.pdf")