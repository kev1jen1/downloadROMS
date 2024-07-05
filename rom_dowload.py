from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.romsgames.net/roms/nintendo/")

driver.implicitly_wait(10)
element = driver.find_element(By.TAG_NAME, 'section')
elements = element.find_elements(By.TAG_NAME, "a")

stoppp = False
i = 0
# Use index to keep track of the current element
while stoppp == False:
    # Re-acquire the element list after navigation
    element = driver.find_element(By.TAG_NAME, 'section')
    elements = element.find_elements(By.TAG_NAME, "a")

    e = elements[i]
    print(e.text)
    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", e)
    time.sleep(1)  # Pause to ensure scrolling is complete
    # Click the element using JavaScript
    driver.execute_script("arguments[0].click();", e)
    print(i)
    i += 1
    if e == 'next':
        print("next")
    else:
        time.sleep(1)  # Pause to allow the page to load after click
        driver.back()
        time.sleep(1)  # Pause to allow the previous page to load

time.sleep(100)
driver.quit()
