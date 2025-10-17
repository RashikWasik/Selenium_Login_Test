from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = Service("E:chromedriver.exe")  # Update your path
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Invalid Login Test
driver.get("https://practicetestautomation.com/practice-test-login/")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.ID, "submit")

# Enter invalid credentials
username_field.send_keys("wronguser")
password_field.send_keys("wrongpass")
submit_button.click()

time.sleep(2)

check = "Your username is invalid!"

# Validate error message
try:
    error_message = driver.find_element(By.ID, "error").text
    if check in error_message:
        print("Test Passed: Invalid login shows error message.")
    else:
        print("Test Failed: Error message not displayed correctly.")
except:
    print("Test Failed: Error message element not found.")

#End
driver.quit()