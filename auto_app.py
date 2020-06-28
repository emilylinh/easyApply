import getpass

# Import webdriver for automation
from selenium import webdriver

# Import Keys to emulate the keyboard keys to nagivate the webdriver
from selenium.webdriver.common.keys import Keys

# Importing the ChromeDriver class for handling webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.linkedin.com/jobs/?showJobAlertsModal=false')

# Nagivates to the LinkedIn login page 
driver.find_element_by_xpath('/html/body/nav/a[3]').click()

# Retrieves login info from user input 
email = input('Enter your email or phone number: ')
pwd = getpass.getpass(prompt='Enter your password: ')

# Logins into LinkedIn
driver.find_element_by_xpath('//*[@id="username"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()


job_search = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember17"]')
job_search.send_keys('data analyst') # Modify job title here 

loc_search = driver.find_element_by_xpath('//*[@id="jobs-search-box-location-id-ember17"]')
loc_search.send_keys('United States') # Modify location here 

driver.find_element_by_xpath('//*[@id="ember17"]/button').click() # Clicks Search button 



