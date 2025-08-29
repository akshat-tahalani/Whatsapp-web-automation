from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Tahal\AppData\Local\Google\Chrome\User Data\Default")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com/")

# Wait for search box to be ready
wait = WebDriverWait(driver, 30)
search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='textbox'][data-tab='3']")))

search_box.click()
search_box.send_keys("akki bhaiya")  # Replace with real contact name

time.sleep(2)

search_box.send_keys(Keys.ENTER)

print("yo wassup ")

message_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']")))
message_box.click()

message_box.send_keys("this is an automated message with an optiional image attached")

message_box.send_keys(Keys.ENTER)

time.sleep(5)

print("msh bhej diya ")

#attach_button = driver.find_element(By.XPATH, "//span[@title='Plus rounded']")
#attach_button.click()

#photos_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Photos & Videos')]")
#photos_button.click()
file_input  = driver.find_element(By.CSS_SELECTOR,"input[type='file'][accept*='image']")

image_path = r"C:\Users\Tahal\OneDrive\Pictures\wallpapers\wallhaven-yxwozk_3440x1440.png"
file_input.send_keys(image_path)
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()

time.sleep(10)
