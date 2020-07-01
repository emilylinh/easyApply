import getpass
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from BeautifulSoup import BeautifulSoup
import requests 

# Import webdriver for automation
from selenium import webdriver

# Import Keys to emulate the keyboard keys to nagivate the webdriver
from selenium.webdriver.common.keys import Keys

# Importing the ChromeDriver class for handling webdriver
from webdriver_manager.chrome import ChromeDriverManager

class easyApply:
    """
    Allows user to apply all jobs filtered by key-search word(s) and location posted in the past week
    under the LinkedIn EasyApply option. 
    """

    def __init__(self, user, pwd, driver, keyword, job_loc, max_page):
        self.user = user
        self.pwd = pwd 
        self.driver = driver 
        self.job_title = keyword
        self.job_loc = job_loc
        self.max_page = max_page

    # Logins into LinkedIn -  WORK IN PROG.
    # NEED to factor in load time 
    def login(self):
        driver = self.driver  
        driver.find_element_by_xpath('/html/body/nav/a[3]').click() # Clicks sign-in button  

        driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.user) # Enters user
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.pwd) # Enters pwd 

        driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()
    
    # Enters in job search preference  -  WORK IN PROG.
    # SHOULD revisit to properly find href links by parsing through family tree instead 
    # of just find element by xpath since LinkedIn could change these id names any time  
    def search_filer(self):
        driver = self.driver 

        job_search = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember17"]')
        job_search.send_keys(self.job_title) 

        loc_search = driver.find_element_by_xpath('//*[@id="jobs-search-box-location-id-ember17"]')
        loc_search.send_keys(self.job_loc) 

        driver.find_element_by_xpath('//*[@id="ember17"]/button').click() # Clicks Search button 

        # Select easyApply option under LinkedIn features 
        driver.find_element_by_xpath('//*[@id="ember1332"]/span').click() # Clicks LinkedIn Features button
        driver.find_element_by_xpath('//*[@id="ember1334"]/li[1]/label').click() # Clicks "Easy Apply"
        driver.find_element_by_xpath('//*[@id="ember1340"]/span').click() # Clicks "Apply"

        # Filters for jobs posted this past week 
        driver.find_element_by_xpath('//*[@id="ember1761"]/span').click() # Clicks "Date Posted"
        driver.find_element_by_xpath('//*[@id="ember1763"]/li[2]/label').click() # Clicks this "Past Week"
        driver.find_element_by_xpath('//*[@id="ember1766"]/span').click()

    # Applies for each job  -  WORK IN PROG.
    # perhaps parse html using BeautifulSoup to search for each job link (total of 25 jobs/webpage) and webpage 
    # NEED TO slow down the process so LinkedIn doesn't auto-detect the bot
    def jobApply(self):
        driver = self.driver 
        # login()
        # search_filer()





driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.linkedin.com/jobs')

# Retrieves login and search info from user input // temporary for testing purposes 
user = input('Your email or phone number: ')
pwd = getpass.getpass(prompt='Enter your password: ')
keyword = input('Search keyword(s) i.e. "data analyst + entry level": ') 
job_loc = input('Job Location: ') 
max_page = input('No. of Page(s) [25 jobs/page]: ')



