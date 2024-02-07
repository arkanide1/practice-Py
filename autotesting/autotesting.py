# import time
# from selenium import webdriver

# chrome_browser = webdriver.Chrome()

# chrome_browser.maximize_window()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.python.org")
# print("Welcome to Python.org" in driver.title)
# easier way to check our code is to use assert instead of print
# if false it closes the tab and gives err


assert ("Welcome to Python.org" in driver.title)


# for the body of the page we can use selectors eg:
css_btn = driver.find_element(By.CLASS_NAME, "donate-button")

print(css_btn.get_attribute('innerHTML'))
search_field = driver.find_element(By.ID, "id-search-field")
# another useful thing indead of (by.id) or (by.classname) we can use css selector
search_field.clear()  # to clear the inp
search_field.send_keys("selenium")
search_field.send_keys(Keys.RETURN)


assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
input("Press Enter to close the browser...")
driver.close()
