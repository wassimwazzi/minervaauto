from selenium import webdriver
import time
from credentials import USERNAME, PASSWORD, CRN

def enter_crn(crn):
  # scroll down to the bottom of the page
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  # Find the element where you need to enter the CRN of the course
  crn_field = driver.find_element("id", "crn_id1")

  # Enter the CRN of the course
  crn_field.send_keys(crn)

  time.sleep(2)
  # Find the button to submit the course registration form and click it
  register_button = driver.find_element("xpath", "//input[@value='Submit Changes']")
  register_button.click()

  # Press enter
  # crn_field.send_keys(webdriver.common.keys.Keys.ENTER)
  # press('enter')

def check_success():
  # If the text "Registration Add Errors" is found in the page, then the course was not added
  return not ("Registration Add Errors" in driver.page_source)

# CONSTANTS
WAIT_BETWEEN_FAILURE = 60 # seconds
  

# Set up the webdriver to open a new Chrome browser window
options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

# Navigate to the Minerva login page
driver.get("https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin")

time.sleep(15)

# Find the elements where you need to enter your login credentials
username_field = driver.find_element("id", "mcg_un")
password_field = driver.find_element("id","mcg_pw")

# Enter your login credentials
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

# Find the login button and click it
login_button = driver.find_element("id", "mcg_un_submit")
login_button.click()

# Navigate to the course registration page on Minerva
driver.get("https://horizon.mcgill.ca/pban1/bwskfreg.P_AltPin")

# Select the current term by clicking on the submit button
# find element by html value
submit_field = driver.find_element("xpath", "//input[@value='Submit']")
submit_field.click()

success = False
while not success:
  enter_crn(CRN) # submits the form too
  if check_success():
    print("Success!")
    success = True
  else:
    print("Failure, trying again in {} seconds".format(WAIT_BETWEEN_FAILURE))
    time.sleep(WAIT_BETWEEN_FAILURE)


# Close the browser window
driver.quit()
