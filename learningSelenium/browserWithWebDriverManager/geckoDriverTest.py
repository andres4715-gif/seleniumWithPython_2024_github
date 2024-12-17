from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://selenium.dev")
driver.maximize_window()
title = driver.title
print("✅", title)

driver.close()
driver.quit()