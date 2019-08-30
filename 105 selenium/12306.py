from Chaojiying import run
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# bro = webdriver.Chrome(executable_path='/Users/henry/Downloads/Tools/chromedriver', options=chrome_options)
bro = webdriver.Chrome(executable_path='/Users/henry/Downloads/Tools/chromedriver')

bro.get('https://kyfw.12306.cn/otn/resources/login.html')
sleep(5)
bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
sleep(5)
bro.save_screenshot('main.png')

image = bro.find_element_by_id('J-loginImg')
xy = image.location
size = image.size
print(xy, size)

rect = (int(xy['x']), int(xy['y']), int(xy['x'] + size['width']), int(xy['y'] + size['height']))

i = Image.open('main.png')
code = i.crop(rect)
code.save('code.png')

# 调用超级鹰
xoy = run('code.png', 9004)
xoy_li = xoy.split('|')
for xy in xoy_li:
    x, y = xy.split(',')
    print(x, y, '验证码坐标')
    webdriver.ActionChains(bro).move_to_element_with_offset(image, int(x), int(y)).click().perform()
    sleep(1)

print('done')
