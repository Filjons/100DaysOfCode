Skip to content
 
Search…
All gists
Back to GitHub
Sign in
Sign up
Instantly share code, notes, and snippets.

@TheMuellenator
TheMuellenator/main.py Secret
Forked from angelabauer/main.py
Last active 4 hours ago
Code
Revisions
4
Stars
4
Forks
8
Clone this repository at &lt;script src=&quot;https://gist.github.com/TheMuellenator/850fa1306944f6576a37e65323fb2b76.js&quot;&gt;&lt;/script&gt;
<script src="https://gist.github.com/TheMuellenator/850fa1306944f6576a37e65323fb2b76.js"></script>
Day 49 L395 - Sign into LinkedIn
main.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "YOUR_EMAIL_HERE"
ACCOUNT_PASSWORD = 'YOUR_PW_HERE'

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")
@itsrabinbhat
itsrabinbhat commented on May 27
while trying to scrape amazon or linkedin, I'm prompted to solve the captcha.
any solution to that?

@Niranjan-pavlov
Niranjan-pavlov commented on Jul 18
good luck making that!!

@DrWhite369
DrWhite369 commented on Jul 18
hey where is every one

@sanskaryo
sanskaryo commented on Jul 21
good and simple code bro thx , i didnt had the cookies part in mine

@Harsha0130
Harsha0130 commented on Jul 23
Here is my code:
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import os
import time

EMAIl = os.environ["Email"]
PASSWORD = os.environ["Password"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3962661047&f_"
"AL=true&geoId=105214831&keywords=python%20developer&location=Bengaluru"
"%2C%20Karnataka%2C%20India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

signin = driver.find_element(By.CLASS_NAME, value="btn-secondary-emphasis")
signin.click()

time.sleep(2)

email = driver.find_element(By.ID, value="username")
email.send_keys(EMAIl)

password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)

enter = driver.find_element(By.CLASS_NAME, value="from__button--floating")
enter.click()

@PaulPeter01
PaulPeter01 commented on Jul 26
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USER_EMAIL = "MY_EMAIL"
USER_PASSWORD = "MY_PASSWORD"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3982452213&"
"keywords=oil%20gas&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true")

time.sleep(2)

def sign_in():
sign_in_but = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_but.click()
email_input = driver.find_element(by=By.ID, value="username")
email_input.send_keys(USER_EMAIL)
password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(USER_PASSWORD)
sign = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign.click()

sign_in()

@ValentynChornomaz
ValentynChornomaz commented on Aug 2
Dude, isn't that supposed to be a python course? Why do I feel it's becoming more and more web development course?

@Anan014
Anan014 commented on Aug 24
I have solved it like this

Solution: Automating LinkedIn Job Application Login with Selenium
In this solution, I automate the process of logging into LinkedIn and accessing a specific job search page using Selenium. The script waits for elements to become clickable before interacting with them, ensuring a smooth automation flow. Below is the code I used:


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Load environment variables from the specified .env file
load_dotenv("../env/day49_env.env")

# Retrieve login credentials and target URL from environment variables
ACCOUNT_EMAIL = os.getenv("EMAIL_ADDRESS")
ACCOUNT_PASSWORD = os.getenv("PASSWORD")
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3997729777&f_AL=true&f_PP=101570771&keywords=Python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

# Set Chrome options to keep the browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the LinkedIn job search page
driver.get(URL)

# Use WebDriverWait to wait for elements to become clickable and interact with them
wait = WebDriverWait(driver,20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis"))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(ACCOUNT_EMAIL)
wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(ACCOUNT_PASSWORD)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
Explanation:
Environment Variables: The script retrieves the LinkedIn email and password from an .env file for security reasons, keeping sensitive information out of the source code.
WebDriver Configuration: The script uses webdriver.ChromeOptions() to keep the browser window open after the script completes, which is useful for debugging and verifying the automation steps.
WebDriverWait: This is used to ensure that the script waits for the necessary elements to load and become interactive before attempting any actions, preventing errors due to elements not being ready.

@my-road-to-code
my-road-to-code commented 3 weeks ago
I found that the LinkedIn links were inconsistent to where they opened up to. The same link will give open 3 different pages. Is there anyway to make it more consistent or is this LinkedIn combating bots?
image
image
image

@Akhilesh1426
Akhilesh1426 commented 2 weeks ago
same brother

 to join this conversation on GitHub. Already have an account? Sign in to comment
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
