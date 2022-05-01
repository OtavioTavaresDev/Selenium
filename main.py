# Selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("python")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
