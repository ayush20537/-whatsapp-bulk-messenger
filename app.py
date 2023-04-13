# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

# Config
login_time = 30  # Time for login (in seconds)
new_msg_time = 8  # Time for a new message (in seconds)
send_msg_time = 10  # Time for sending a message (in seconds)
country_code = 91  # Set your country code

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Read numbers from file
with open('numbers.txt', 'r') as file:
    numbers = file.readlines()

# Encode Message Text
with open('message.txt', 'r') as file:
    msg = quote(file.read())

# Loop Through Numbers List
for i, num in enumerate(numbers):
    num = num.strip()

    link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
    driver.get(link)
    time.sleep(new_msg_time)

    # Handle alert
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
    except:
        pass

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(send_msg_time)

# Wait for the last message to be sent before quitting
time.sleep(send_msg_time)

# Quit the driver
driver.quit()
