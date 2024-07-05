from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# https://sites.google.com/chromium.org/driver/
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.romsgames.net/roms/nintendo/")

driver.implicitly_wait(10)

index = 0
i = 0
# Use index to keep track of the current element
while index != 50:
    # Re-acquire the element list after navigation
    element = driver.find_element(By.TAG_NAME, 'section')
    elements = element.find_elements(By.TAG_NAME, "a")

    if i >= len(elements):
        break

    e = elements[i]
    print(e.text)
    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", e)
    time.sleep(1)  # Pause to ensure scrolling is complete

    # Check if the text of the element is "Next" before clicking
    if e.text == 'Next':
        print("nexteee")
        driver.execute_script("arguments[0].click();", e)
        time.sleep(3)  # Pause to allow the next page to load
        i = 0  # Reset the index to 0 to start over with the new elements
    else:
        # Click the element using JavaScript
        driver.execute_script("arguments[0].click();", e)
        print(index)
        i += 1
        index += 1
        time.sleep(1)  # Pause to allow the page to load after click
        driver.back()
        time.sleep(1)  # Pause to allow the previous page to load

time.sleep(100)
driver.quit()

