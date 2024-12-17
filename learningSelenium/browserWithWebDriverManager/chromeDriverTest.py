from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("http://www.rcvacademy.com")
driver.get("http://selenium.dev")
driver.maximize_window()
title = driver.title
print("✅", title)

driver.close()
driver.quit()