from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.mapmyride.com/my_home/")

username_input = driver.find_element_by_id('email')
username_input.send_keys("")
pwd_input = driver.find_element_by_id('password')
pwd_input.send_keys("")
submit_button = driver.find_elements_by_xpath('//*[@id="root"]/div/div[3]/div/div/form/button')[0]
submit_button.click()
time.sleep(5)
dashboard_link=driver.find_element_by_xpath('//*[@id="dashboard_tab"]/a')
dashboard_link.click()
calendar_link=driver.find_element_by_xpath('//*[@id="user_dashboard_links"]/header/a[2]')
calendar_link.click()
