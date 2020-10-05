# !/usr/bin/python
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
#import asyncio
from time import gmtime, strftime, ctime
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.pixnet.net')
#print (driver.title)
assert (driver.title) == '痞客邦' , 'PIXNET->故障'

driver.get('https://billboard.events.pixnet.net/')
#print (driver.title)
assert (driver.title) == 'Xboard' , 'PIXXboard->故障'

driver.get('https://www.pixnet.net/blog')
#print (driver.title)
assert (driver.title) == '部落格首頁 痞客邦' , 'PIX部落格->故障'

driver.get('https://streamtopic.pixnet.net/')
#print (driver.title)
assert (driver.title) == ':: 痞客邦 邦邦 - 你的興趣話題交流圈 ::' , 'PIX邦邦->故障'

driver.get('https://styleme.pixnet.net/home')
#print (driver.title)
assert (driver.title) == '潮流、美妝、消費 創造個人化風格的女性社群 PIXstyleMe' , 'PIXstyleMe->故障'

driver.get('https://m.pixgoods.pixnet.net/')
#print (driver.title)
assert (driver.title) == 'PIXgoods｜痞客邦購物為你的生活帶來更多便利與美好' , 'PIXgoods->故障'

driver.get('https://food.pixnet.net/')
#print (driver.title)
assert (driver.title) == '痞客邦美食 痞客邦' , 'PIX美食->故障'

time.sleep(3)
driver.close()
