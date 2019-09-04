# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(executable_path='/Users/henry/Downloads/Tools/chromedriver', chrome_options=options)
driver.get('http://www.baidu.com')
builder = ActionChains(driver)
builder.key_down(Keys.F12).perform()
sleep(5)
driver.quit()
