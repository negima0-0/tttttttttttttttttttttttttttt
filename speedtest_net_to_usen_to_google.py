# -*- coding: utf-8 -*-
from selenium import webdriver #4.16.0
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
import time
import os
import openpyxl
from openpyxl.drawing.image import Image

# driver起動.
driver = webdriver.Chrome()

# wait明示処理(それぞれでタイムアウト指定してるからいらない説).
driver.implicitly_wait(30)

#ページ遷移.
driver.get('https://www.speedtest.net/ja')
print('pages_open')

#ss取るためのページサイズ変更(見切れ防止に一応(いらないかも？)).
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)

#各特定要素が表示されるまで待機.
print('try to test')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'start-text')))
#go ボタンクリック.
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
button_elements = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
time.sleep(30)
WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')))
if driver.find_element(By.XPATH,
                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button'):
    driver.find_element(By.XPATH,
                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button').click()
    time.sleep(3)
    png = driver.find_element(By.XPATH,
                              '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]').screenshot_as_png
#result = driver.find_element(By.CLASS_NAME, 'result-data').get_attribute("textContent")
#スクショ保存.
with open('./ss1.png', 'wb') as f:
    f.write(png)

#-------------------------------------------------------------------------------------------------#

#ページ遷移.
#driver.execute_script("window.open('https://speedtest.gate02.ne.jp/')")
#driver.switch_to.window(driver.window_handles[1])
driver.get('https://speedtest.gate02.ne.jp/')
print('pages_open')

#ss取るためのページサイズ変更(見切れ防止に一応(いらないかも？)).
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)

#各特定要素が表示されるまで待機.
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
print('try to test')
#WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '測定開始')))
#測定開始ボタンクリック.
driver.execute_script('javascript:speedtest.start();')
time.sleep(20)

png = driver.find_element(By.CLASS_NAME, 'speedtest_content').screenshot_as_png
#スクショ保存.
with open('./ss2.png', 'wb') as f:
    f.write(png)

 #------------------------------------------------------------------------------------------------#

#ページ遷移.
#driver.execute_script("window.open('https://www.google.com/search?q=Speedtest&sca_esv=600762144&source=hp&ei=eNavZbnZCZKMvr0P9-2jsAw&iflsig=ANes7DEAAAAAZa_kiElug3oFvA6mNIh56Dzg8yPRcQzf&ved=0ahUKEwi59auS5fODAxUShq8BHff2CMYQ4dUDCA8&uact=5&oq=Speedtest&gs_lp=Egdnd3Mtd2l6IglTcGVlZHRlc3QyEBAAGIAEGIoFGEMYsQMYgwEyBRAAGIAEMgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMgUQABiABDILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgARI4wJQAFgAcAB4AJABAJgBRqABRqoBATG4AQPIAQD4AQL4AQE&sclient=gws-wiz')")
#driver.switch_to.window(driver.window_handles[-1])
driver.get('https://www.google.com/search?q=Speedtest&sca_esv=600762144&source=hp&ei=eNavZbnZCZKMvr0P9-2jsAw&iflsig=ANes7DEAAAAAZa_kiElug3oFvA6mNIh56Dzg8yPRcQzf&ved=0ahUKEwi59auS5fODAxUShq8BHff2CMYQ4dUDCA8&uact=5&oq=Speedtest&gs_lp=Egdnd3Mtd2l6IglTcGVlZHRlc3QyEBAAGIAEGIoFGEMYsQMYgwEyBRAAGIAEMgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMgUQABiABDILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgARI4wJQAFgAcAB4AJABAJgBRqABRqoBATG4AQPIAQD4AQL4AQE&sclient=gws-wiz')
print('pages_open')

#ss取るためのページサイズ変更(見切れ防止に一応(いらないかも？)).
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)

#各特定要素が表示されるまで待機.
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
print('try to test')
#測定開始ボタンが表示されるまで待機.
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'lv7K9c')))
#測定開始ボタンクリック.
driver.find_element(By.CLASS_NAME, 'lv7K9c').click()

time.sleep(20)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'BbqFQc')))
png = driver.find_element(By.CLASS_NAME, 'fn1k4').screenshot_as_png
#スクショ保存.
with open('./ss3.png', 'wb') as f:
    f.write(png)

driver.close()
driver.quit()

#excle 貼り付け.
if not os.path.isfile('check.xlsx'):
    print(f"ファイルチェックエラー: '{check.xlsx}' は存在しません。")
    exit()

wb = openpyxl.load_workbook('check.xlsx')
ws = wb["Sheet1"]

speedtest_img = Image('ss1.png')
usen_img = Image('ss2.png')
googole_img = Image('ss3.png')

ws.add_image(speedtest_img, 'A1')
ws.add_image(speedtest_img, 'A2')
ws.add_image(speedtest_img, 'A3')

wb.save('check.xlsx')
