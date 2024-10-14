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
9
Clone this repository at &lt;script src=&quot;https://gist.github.com/TheMuellenator/3cc1fdb5f43db6c5d1dd8f773fa4b05c.js&quot;&gt;&lt;/script&gt;
<script src="https://gist.github.com/TheMuellenator/3cc1fdb5f43db6c5d1dd8f773fa4b05c.js"></script>
Day 49 L397 - Apply for all jobs
main.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = YOUR LOGIN EMAIL
ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD
PHONE = YOUR PHONE NUMBER


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

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

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
@akumarm23
akumarm23 commented on Dec 13, 2023
Was very helpful, thank you!

@ndtwx
ndtwx commented on Dec 21, 2023
image
Hi guys. i'm facing this issue. not sure how to fix it

@AliDraz
AliDraz commented on Jan 9
If someone have problem like on listing.click method
basically whats happening is the function go further put your number on the feild then click on next then click on close button and ask you to discard and save option unfortunatlly there is no code for click that buttion just type 2 line of code just next to the close_button which is on 86 line.
save_button = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div[3]/button[2]/span")
save_button.click()
These two lines will work for you and click on save button you are good to go

@nevergiveup777
nevergiveup777 commented on Jan 22
I like the idea of this project but I can't find enough job offers with a one-step application that is worth the time of automating it in this way.

@visualos
visualos commented on Feb 7
of this project but I can't find enough job offers with a one-step application that is worth the time of automating it in this wa

same here

@AliDraz
AliDraz commented on Feb 7
I like the idea of this project but I can't find enough job offers with a one-step application that is worth the time of automating it in this way.

This is just for practise to make things automatic.
Just little bit research make it more useful and automate some other things like automatic data entry.
Get data from online website and create tables

@pjavierdicillo
pjavierdicillo commented on Mar 5
I like the idea of this project but I can't find enough job offers with a one-step application that is worth the time of automating it in this way.

I found the same, unfortunately. Probably, companies add multi-step applications with customised questions to avoid bots making the applications.

@guitarlass
guitarlass commented on Mar 9
Unfortunately, yes.
@ndtwx ndtwx you could try increasing the width of the window. If the button is not showing up on the screen, Python cannot handle it.
driver.set_window_size(1400, driver.get_window_size()['height'])

@Mayday46
Mayday46 commented on Mar 11
Navigate to Linkedin
driver.get("https://www.linkedin.com/")

Sign In
signinButton = driver.find_element(By.LINK_TEXT, "Sign in")
signinButton.click()

Username
userId = driver.find_element(By.ID, "username")
userId.send_keys(email)

Password
userPassword = driver.find_element(By.ID, 'password')
userPassword.send_keys(password, Keys.ENTER)

Search
search = driver.find_element(By.CSS_SELECTOR, "#global-nav-search > div > button > div")
search.click()
inputBox = driver.find_element(By.CSS_SELECTOR, "#global-nav-typeahead > input")
inputBox.send_keys(jobNames, Keys.ENTER)

jobButton = driver.find_element(By.CSS_SELECTOR, "#a11y-content > div > div > main > div > div > section > div > ul > li:nth-child(3) > a")
jobButton.click()

Im having a hardtime fixitng the jobButton. I tired to copy the Xpath, selector from the chrome devtools, but it seems no help. PLEASE HELP ME

@la-23
la-23 commented on Apr 7
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

os.environ["wachtwoord"] = "Luipaard123"
wachtwoord = os.environ["wachtwoord"]
phone_number = ("088344422")

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=web_options)
driver.get(URL)
time.sleep(3)
current_url = driver.current_url.split("https://")[1]

def login_page():
driver.find_element(By.XPATH, value="//[@id='session_key']").send_keys("Luffytest4@hotmail.com")
driver.find_element(By.XPATH, value="//[@id='session_password']").send_keys(wachtwoord)
driver.find_element(By.XPATH, value="//*[@id='main-content']/section/div/div/form/div/button").click()
driver.get(url=URL)
time.sleep(20)

def search_page_login():
driver.find_element(By.XPATH, value="//[@id='main-content']/section/section/div/a").click()
driver.find_element(By.XPATH, value="//[@id='username']").send_keys("Luffytest4@hotmail.com")
driver.find_element(By.XPATH, value="//[@id='password']").send_keys(wachtwoord)
driver.find_element(By.XPATH, value="//[@id='organic-div']/form/div/button").click()
time.sleep(25)
all_apllications = driver.find_elements(By.XPATH,value='//div[contains(@Class, "job-card-container--clickable")]')
test = len(all_apllications)
return all_apllications

def search_jobs(all_apllications):
print(len(all_apllications))
for job in all_apllications:
job.click()
time.sleep(5)
try:
aplied_link = driver.find_element(By.XPATH,'//a[contains(@Class, "jobs-s-apply__application-link")]').text

    except NoSuchElementException:
        time.sleep(2)
        easy_appply = driver.find_element(By.XPATH, '//button[starts-with(@class, "jobs-apply-button")]').click()
        time.sleep(2)
        phone_number = driver.find_element(By.XPATH, '//input[contains(@class, "artdeco-text-input--input")]')
        if phone_number.text == "":
            phone_number.send_keys("0466882232")
        button = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button--primary")]')

        if button.text == "Next":
            close = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button artdeco-button--circle")]')
            close.click()
            discard = driver.find_element(By.XPATH,"//button[contains(@class, 'artdeco-button--secondary')]")
            discard.click()
            continue
        else :
            button.click()


        # buttons_save = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button--primary")]')
        # actions = ActionChains(driver)
        # actions.move_to_element(buttons_save).click().perform()
        # time.sleep(7)
        # button.click()
        # time.sleep(8)  # er is een vraag die manueel moet gaan beantwoorden,
        # review = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button--primary")]')
        # review.click()
        # time.sleep(7)
        # de redenen waarrom de submit,nexten reviuew button het ongeveer hetzelde eruit zien is dat het dezelfde klassen heeft
        # waar de computer weet pas waar de submitbutton is wanneer je op die review butoon klikt want dan gaat het naar een andere pagina en update het
        # het html code . dus je kunt de submit nog niet opvooran difienier want het bestaat nog niet om het nog niet op de submit pagina zijn.
        # submit = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button--primary")]')
        # submit.click()
        # time.sleep(7)
        # done = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button--primary")]')
        # done.click()

    else:
        if aplied_link == aplied_link:
            print("############")
            print(aplied_link)
            continue
    finally:
        print("next job")
print(current_url)
als je direct naar de login pagina word gestuurd
if "www.linkedin.com/" == current_url:
login_page()
all_aplications = search_page_login()
search_jobs(all_aplications)
else:
all_apllications = search_page_login()
print(search_jobs(all_apllications))
#
driver.quit()

@thelastmedici
thelastmedici commented on Jun 18
please what is wrong with my code

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = 'horpeyemijoshua@gmail.com'
ACCOUNT_PASSWORD ='123Jesus'
PHONE = '+2348131061074'

def abort_application():
# Click Close Button
close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
close_button.click()

time.sleep(2)
# Click Discard Button
discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
discard_button.click()
Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3927829027&f_AL=true&f_E=2&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()
Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")
Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div['

@adi-devv
adi-devv commented on Jun 28
Check out my code, I built it from scratch and it doesn't require a captcha.

https://github.com/adi-devv/Sele-nium/blob/main/LinkedInAutoApply.py

@MinaEmad2024
MinaEmad2024 commented on Jul 13
I made the project to save all jobs ,
it works fine except it can't loop through al the jobs in the left side panel and it give the following error message,
`
Traceback (most recent call last):
File "C:\Users\DRMINA2019\PycharmProjects\day 50 linkedlin job application.venv\Scripts\main.py", line 42, in
job.click()
File "C:\Users\DRMINA2019\PycharmProjects\day 50 linkedlin job application.venv\Lib\site-packages\selenium\webdriver\remote\webelement.py", line 94, in click
self._execute(Command.CLICK_ELEMENT)
File "C:\Users\DRMINA2019\PycharmProjects\day 50 linkedlin job application.venv\Lib\site-packages\selenium\webdriver\remote\webelement.py", line 395, in _execute
return self._parent.execute(command, params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\DRMINA2019\PycharmProjects\day 50 linkedlin job application.venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 354, in execute
self.error_handler.check_response(response)
File "C:\Users\DRMINA2019\PycharmProjects\day 50 linkedlin job application.venv\Lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 229, in check_response
raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
(Session info: MicrosoftEdge=126.0.2592.87); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#stale-element-reference-exception
Stacktrace:
GetHandleVerifier [0x00007FF6CA008132+13538]
Microsoft::Applications::Events::EventProperty::~EventProperty [0x00007FF6C9F91DE9+595465]
(No symbol) [0x00007FF6C9DAE6CF]
(No symbol) [0x00007FF6C9DB37C9]
(No symbol) [0x00007FF6C9DB56CB]
(No symbol) [0x00007FF6C9DB5770]
(No symbol) [0x00007FF6C9DF440F]
(No symbol) [0x00007FF6C9DE85E6]
(No symbol) [0x00007FF6C9E11FFA]
(No symbol) [0x00007FF6C9DE8147]
(No symbol) [0x00007FF6C9DE800D]
(No symbol) [0x00007FF6C9E122E0]
(No symbol) [0x00007FF6C9DE8147]
(No symbol) [0x00007FF6C9E2B1EE]
(No symbol) [0x00007FF6C9E11C63]
(No symbol) [0x00007FF6C9DE766E]
(No symbol) [0x00007FF6C9DE683C]
(No symbol) [0x00007FF6C9DE7221]
Microsoft::Applications::Events::EventProperty::to_string [0x00007FF6CA1C96D4+1099860]
Microsoft::Applications::Events::EventProperty::~EventProperty [0x00007FF6C9F0D8FC+53532]
Microsoft::Applications::Events::EventProperty::~EventProperty [0x00007FF6C9F00E25+1605]
Microsoft::Applications::Events::EventProperty::to_string [0x00007FF6CA1C8665+1095653]
Microsoft::Applications::Events::ILogConfiguration::operator* [0x00007FF6C9F9C961+27777]
Microsoft::Applications::Events::ILogConfiguration::operator* [0x00007FF6C9F96CE4+4100]
Microsoft::Applications::Events::ILogConfiguration::operator* [0x00007FF6C9F96E1B+4411]
Microsoft::Applications::Events::EventProperty::~EventProperty [0x00007FF6C9F8CFA0+575424]
BaseThreadInitThunk [0x00007FF84FA0257D+29]
RtlUserThreadStart [0x00007FF8512EAF28+40]

`
so what does that mean? and how to solve it?

@SoraK93
SoraK93 commented on Jul 24 • 
"""Code for Save and Follow all job in the list. It will change pages and continue its function.
If i can improve my code somewhere please guide me on that.
I found that taking a little bit more time on sleep() function helps the page to load and due to which I was not getting "NoSuchElementException" anymore randomly."""

`import os
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import time

load_dotenv()

<--- REQUIRED DATA TO RUN THE PROGRAM --->
USERNAME = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]
LINK = os.environ["SITE"]

<--- SAVE & FOLLOW FUNCTION --->
def save_follow():
# <--- SAVE & IF ALREADY SAVED MOVE TO NEXT JOB LISTING --->
save = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
if save.text.split()[0] == "Save":
save.click()
time.sleep(2)
else:
pass
try:
follow = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Follow"]')
ActionChains(driver).scroll_to_element(follow).click(follow).perform()
# <--- FOLLOW & IF ALREADY FOLLOWING MOVE TO NEXT JOB LISTING --->
# <---Below error occurs if already following, python wont find the follow button since its changed to following--->
except NoSuchElementException:
# <--- CONFIRMING VISUALLY IF ALREADY FOLLOWING --->
following = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Following"]')
ActionChains(driver).scroll_to_element(following).perform()
pass

<--- JOB SEARCH FUNCTION--->
def job_search_func(job_search):
time.sleep(5)
# <--- SEARCH THROUGH JOB LIST & SAVE/ FOLLOW ALL THE JOBS FOR LATER VIEW--->
for li in job_search:
ActionChains(driver).scroll_to_element(li).click(li).perform()
time.sleep(2)
save_follow()
time.sleep(2)

<--- CHROME SETUP --->
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.maximize_window()

<--- OPEN SITE --->
sometimes opens up https://www.linkedin.com/ i dont understand why. cause of which you might need to re-run
driver.get(LINK)

<--- LOGIN --->
time.sleep(2)
driver.find_element(By.LINK_TEXT, value="Sign in").click()
time.sleep(5)
driver.find_element(By.ID, value="username").send_keys(USERNAME)
driver.find_element(By.ID, value="password").send_keys(PASSWORD, Keys.ENTER)

<--- CAPTCHA - MANUAL INPUT REQUIRED HERE --->
input("Press Enter when you have solved the Captcha")

<---Using total number of results % max results in a page to get the number of pages for our search
I was trying to get a list of pages just like "job search" below, but the output was an empty result so this is a work around for that
search_result = int(driver.find_element(By.CSS_SELECTOR, value=".jobs-search-results-list__subtitle").text.split()[0])
max_results_in_a_page = 20

"+1" is used cause of how the range function works. if our search_result < 20 then this "+1" can cover for that.
for n in range(search_result % max_results_in_a_page + 1):
page_ul = driver.find_element(By.CSS_SELECTOR, value=f'li[data-test-pagination-page-btn="{n + 1}"]')
time.sleep(3)
ActionChains(driver).scroll_to_element(page_ul).click(page_ul).perform()
time.sleep(2)
job_search = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")
job_search_func(job_search)
`

@madelinecambo
madelinecambo commented on Aug 31
I like the idea of this project but I can't find enough job offers with a one-step application that is worth the time of automating it in this way.

I've found the same thing!

@jahir01khan
jahir01khan commented on Sep 7
I like the idea of this project but I can't find enough job offers with a one-step application that is worth the time of automating it in this way.

"The concept is great, but it is designed with our current skill level in mind. One-step verification jobs are few and far between, which is why my code just looped through the entire list and ended with a bunch of "This application form is too complex, I am skipping this one".
skipping this one

@Convl
Convl commented on Sep 9 • 
I chose to save the job listings and follow the employer instead, which came with its own set of challenges. My code below is functional as of 9/9/2024, for the German version of linkedin. For the english version, you will, at minimum, have to replace the strings "Gespeichert" and "Follower:in" as well as the url of the job search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time
import os
import dotenv

# Go to Linkedin login page, retrieve login credentials from .env file, log in
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login/de?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
dotenv.load_dotenv()
linkedin_username = os.environ.get("LINKEDIN_USERNAME")
linkedin_password = os.environ.get("LINKEDIN_PASSWORD")
username_input.send_keys(linkedin_username)
password_input.send_keys(f"{linkedin_password}{Keys.ENTER}")

# Go to job listings page, wait for it to load, get the div which contains all the job postings, 
# also get a list of all the actual job postings
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3995277407&f_AL=true&keywords=python%20entwickler&origin=JOB_SEARCH_PAGE_JOB_FILTER")
time.sleep(4)
listings_tab = driver.current_window_handle
jobs_div = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")
jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list > ul > li")

# Cycle through all job postings
for job in jobs_list:
    # Click the next job posting so its details open in the pane on the right. This, like all other 
    # commands, will occasionnaly fail with StaleElementReferenceException or ElementClickInterceptedException,
    # so embed it in a try block
    job_link = job.find_element(By.CSS_SELECTOR, "a")
    success_next_job_posting = False
    while not success_next_job_posting:
        try:
            job_link.click()
        except Exception as e:
            print(f"Exception while trying to switch to next job posting: {e}")
        else:
            success_next_job_posting = True    
    time.sleep(1)

    # Check if job is already saved ("Gespeichert" in German, this will vary in other languages), 
    # if not, save it
    success_saving = False
    while not success_saving:
        try:        
            save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
            save_state = save_button.find_element(By.CSS_SELECTOR, "span")
            if save_state.text != "Gespeichert":
                save_button.click()
        except Exception as e:
            print(f"Exception while trying to save job posting: {e}")
        else:
            success_saving = True    

    # Find and open the link to the employer page, switch to that tab and scroll to the top 
    # so that the follow button will be visible
    employer_page = driver.find_element(By.CSS_SELECTOR, ".jobs-search__job-details--wrapper .app-aware-link").get_attribute("href")
    driver.execute_script(f"window.open('{employer_page}');")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, 0);")

    # Check if we are already a follower ("Follower:in" in German, this will vary in other languages), 
    # if not, follow the employer
    success_following = False
    while not success_following:
        try:
            follow_button = driver.find_element(By.CSS_SELECTOR, ".org-company-follow-button")
            follow_state = follow_button.find_element(By.CSS_SELECTOR, "span")
            if follow_state.text != "Follower:in":
                follow_button.click()
        except Exception as e:
            print(f"Exception while trying to follow employer: {e}")
        else:
            success_following = True    

    # Close the new tab, switch back to the tab with the job listings, and scroll down
    # inside the div containing the jobs by the height of the current job listing
    driver.close()
    driver.switch_to.window(listings_tab)
    time.sleep(1)
    driver.execute_script(f"arguments[0].scrollTop += {job.size["height"]}", jobs_div)

driver.quit()
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
