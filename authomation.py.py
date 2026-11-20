
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Open Edge browser
service = Service("msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Open DemoQA webpage
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# Enter user details
driver.find_element(By.ID, "userName").send_keys("Anjana C U")
driver.find_element(By.ID, "userEmail").send_keys("anjana@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Thrissur, Kerala")
driver.find_element(By.ID, "permanentAddress").send_keys("Kolazhy, Thrissur")

# Submit form
driver.find_element(By.ID, "submit").click()

time.sleep(10)

# Verify output
output = driver.find_element(By.ID, "output")

if output.is_displayed():
    print("Form submitted successfully!")
    print(output.text)
else:
    print("Form submission failed!")

# Close browser
driver.quit()
