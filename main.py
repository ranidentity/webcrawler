from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://online.ktmb.com.my/")
try:
    # Wait for the modal to appear (adjust the locator as needed)
    parent_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "announcement-div"))
    )
    elements = parent_div.find_elements(By.XPATH, ".//*")
    for element in elements:
       if (element.tag_name == "button" and
            "payment-modal-btn" in element.get_attribute("class") and
            element.get_attribute("data-dismiss") == "modal" and
            element.text == "OK"):
                element.click()
                print("Button found and clicked!")
                break
    else:
        print("Button not found inside the <div>.")

    # Step 1: Open the dropdown
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection"))
    )
    dropdown.click()

    # Step 2: Locate the search input field and type "JB SENTRAL"
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field"))
    )
    search_input.send_keys("JB SENTRAL")

    # Step 3: Wait for the results to load and select the option
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'JB SENTRAL')]"))
    )
    option.click()

except Exception as e:
    print(f"An error occurred: {e}")

input("Press Enter to close...")
driver.quit()