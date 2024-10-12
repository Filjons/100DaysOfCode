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
Last active 13 hours ago
Code
Revisions
3
Stars
3
Forks
3
Clone this repository at &lt;script src=&quot;https://gist.github.com/TheMuellenator/3518cfb4428494ea5c977ef37efc4727.js&quot;&gt;&lt;/script&gt;
<script src="https://gist.github.com/TheMuellenator/3518cfb4428494ea5c977ef37efc4727.js"></script>
Day 49 L396 - Apply for a job
main.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = YOUR LOGIN EMAIL
ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD
PHONE = YOUR PHONE NUMBER

# Optional - Keep the browser open if the script crashes.
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

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
@egencalp
egencalp commented on Mar 1
After reaching job search page, i cannot continue with press easy apply button. Tried different ways like below, but cannot make my code press the button;
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button--top-card")
apply_button = driver.find_element(by=By.LINK_TEXT, value="Easy apply")

I wonder if it is because of me cannot find the solution or something linkedn did. I gave up on the rest of this project:(

@widmelu
widmelu commented on Mar 9
Same for me. With the code above I was able to locate and click the "Easy Apply" button but am stuck from there on. Unable to locate the "Next" button.

@bssq2
bssq2 commented on Mar 11
here you go. if you want to track each other process and help each other let me know maybe we can find a way to learn...
easy_apply = driver.find_element(By.CSS_SELECTOR, "button.jobs-apply-button.artdeco-button--primary")
easy_apply.click()
next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_button.click()

@Natyman3
Natyman3 commented on Mar 14
try this if you getting different options.

next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_button.click()
next_button.click()

review_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
review_button.click()

submit_application_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
submit_application_button.click()

@nikhiltelase
nikhiltelase commented on Mar 17
check my latest solution>>>

click on sign button
login = driver.find_element(By.LINK_TEXT, value="Sign in")
login.click()

login
email_input = driver.find_element(By.NAME, value="session_key")
email_input.send_keys(email)
password_input = driver.find_element(By.NAME, value="session_password")
password_input.send_keys(password)
login_button = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
login_button.click()

Wait for security check
input("Press Enter when you have solved the Captcha")

apply for first job
job_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
job_apply.click()
next_step1 = driver.find_element(By.CSS_SELECTOR, value=".jobs-easy-apply-content button")
next_step1.click()

next_step2 = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
next_step2.click()

input1 = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017621-numeric")
input1.send_keys("0")
input2 = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017629-numeric")
input2.send_keys("0")

radio_button1 = driver.find_element(By.CSS_SELECTOR, value="#radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017605-multipleChoice label")
radio_button1.click()
radio_button2 = driver.find_element(By.CSS_SELECTOR, value="#radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3843018326-116017645-multipleChoice label")
radio_button2.click()

next_step3 = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
next_step3.click()

submit = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
submit.click()

@sxtcntt
sxtcntt commented on Mar 26 • 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL_LINK = "EMAIL"
PASS_LINK = "PASSWORD"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_path = './Drivers/chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
"&keywords=python%20developer"
"&location=London%2C%20England%2C%20United%20Kingdom"
"&redirect=false&position=1&pageNum=0"
)

time.sleep(2)
reject_button = driver.find_element(by=By.LINK_TEXT, value='Sign in')
reject_button.click()
time.sleep(2)
input_keys = driver.find_elements(By.CSS_SELECTOR, value=".form__input--floating input")
for input_ in input_keys:
if input_.get_attribute(name="id") == "username":
input_.send_keys(EMAIL_LINK)
elif input_.get_attribute(name="id") == "password":
input_.send_keys(PASS_LINK)
button_class = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
button_class.click()

time.sleep(10)

Website check Robo. please click ^_^.
jb_apply = driver.find_element(By.CSS_SELECTOR, value="#main ul li")
jb_apply.click()

time.sleep(2)

jb_apply.click()
button_save = driver.find_elements(By.CSS_SELECTOR, value=".mt5 .display-flex button")
for items in button_save:
if items.get_attribute(name="type") == "button":
items.click()

print("Automate apply CV compelex")

@Tirsvad
Tirsvad commented on Jun 5
If your browser is set to other language than english you can't click on "sign in"! You can change chrome options to force linkedin to accept english instead of the default language

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()
SOLUTION

class AutoApplyJob:
    chrome_options: webdriver.chrome.options.Options
    driver: webdriver

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--lang=en")
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
@Psychodes254
Psychodes254 commented on Jul 19
Honestly, I have tried everything on easy apply but there's no response.

I do think you should update the project, because even if I copy your project to the console, it's not working.

Let me just skip the project.

@DSTHEBEST
DSTHEBEST commented on Aug 5
Honestly, I have tried everything on easy apply but there's no response.

I do think you should update the project, because even if I copy your project to the console, it's not working.

Let me just skip the project.

Hi, I was having the same issue until I went to the father of he div container in which the code for the button is stored and when I used it as
By.CLASS_NAME, it worked
Like just use the class of the div tag just above the button tag

@Anan014
Anan014 commented on Aug 24 • 
Thats my solution and its working

# Import necessary packages
from selenium import webdriver  # To control the web browser
from selenium.webdriver.common.by import By  # To locate elements on the page
from selenium.webdriver.support.ui import WebDriverWait  # To wait for elements to be clickable or visible
from selenium.webdriver.support import expected_conditions as EC  # Conditions for waiting
from dotenv import load_dotenv  # To load environment variables from a .env file
import os  # To access environment variables
from time import sleep  # To pause the execution if needed

# Load environment variables from the .env file
# This is where we store sensitive data like email, password, and URL
load_dotenv("../env/day49_env.env")

# Retrieve credentials and URL from environment variables
ACCOUNT_EMAIL = os.getenv("EMAIL_ADDRESS")  # Email address for login
ACCOUNT_PASSWORD = os.getenv("PASSWORD")  # Password for login
URL = os.getenv("URL")  # URL of the website to automate

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keep the browser open after the script finishes

# Initialize the WebDriver (this opens a Chrome browser)
driver = webdriver.Chrome(options=chrome_options)

# Open the target URL (website's login page)
driver.get(URL)

# Initialize WebDriverWait instance with a 20-second timeout
# This will help us wait for elements to load before interacting with them
wait = WebDriverWait(driver, 20)

# Log in to the account
# Clicks the "Sign in" button, enters the email and password, and submits the form
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis"))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys(ACCOUNT_EMAIL)
wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(ACCOUNT_PASSWORD)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# Reload the URL after login to ensure we're on the correct page
driver.get(URL)

# Start the Easy Apply process
# Clicks the "Easy Apply" button on a job posting
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view"))).click()

# Enter phone number and proceed
# Fills in the phone number and clicks "Next"
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-text-input--input"))).send_keys("0541234567")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()

# Skip the resume upload step (if applicable)
# Clicks "Next" on the resume upload page
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()

# Enter work experience and proceed to review
# Inputs the years of work experience and clicks "Next"
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-text-input--input"))).send_keys("3")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()

# Submit the application
# Finally, clicks the "Submit Application" button
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"))).click()

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
