from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = Service("E:\\chromedriver.exe")  # Update your path
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Valid Login Test
driver.get("https://practicetestautomation.com/practice-test-login/")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.ID, "submit")

# Enter valid credentials
username_field.send_keys("student")
password_field.send_keys("Password123")
submit_button.click()

time.sleep(2)

check = "Logged In Successfully"

# Validate success by element
try:
    success_message = driver.find_element(By.TAG_NAME, "h1").text
    if check in success_message:
        print("Test Passed: Valid login successful.")
    else:
        print("Test Failed: Valid login unsuccessful.")
except:
    print("Test Failed: Success message not found.")

# End
driver.quit()