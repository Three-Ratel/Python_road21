from time import sleep

from selenium import webdriver

bro = webdriver.Chrome(executable_path='/Users/henry/Downloads/Tools/chromedriver')
"""test"""
# bro.get('https://www.jd.com/')
# sleep(3)
# search_input = bro.find_element_by_id('key')
# search_input.send_keys('macPro')
# btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
# btn.click()
# sleep(3)
# jsCode = 'window.scrollTo(0, 0.5*document.body.scrollHeight)'
# bro.execute_script(jsCode)
# sleep(3)
# bro.quit()

"""动态链"""
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
bro.get(url)
bro.switch_to_frame('iframeResult')
div = bro.find_element_by_xpath('//*[@id="draggable"]')
action = webdriver.ActionChains(bro)
for i in range(5):
    print(i+1)
    action.click_and_hold(div).move_by_offset(15, 0).perform()
    sleep(0.5)
print(div)
