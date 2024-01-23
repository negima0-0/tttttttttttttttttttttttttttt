# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# driver起動
driver = webdriver.Chrome()

# wait明示処理(それぞれでタイムアウト指定してるからいらない説)
driver.implicitly_wait(30)

#ページ遷移
driver.get('https://www.google.com/search?q=Speedtest&sca_esv=600762144&source=hp&ei=eNavZbnZCZKMvr0P9-2jsAw&iflsig=ANes7DEAAAAAZa_kiElug3oFvA6mNIh56Dzg8yPRcQzf&ved=0ahUKEwi59auS5fODAxUShq8BHff2CMYQ4dUDCA8&uact=5&oq=Speedtest&gs_lp=Egdnd3Mtd2l6IglTcGVlZHRlc3QyEBAAGIAEGIoFGEMYsQMYgwEyBRAAGIAEMgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMgUQABiABDILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgARI4wJQAFgAcAB4AJABAJgBRqABRqoBATG4AQPIAQD4AQL4AQE&sclient=gws-wiz')
print('pages_open')

#ss取るためのページサイズ変更(見切れ防止に一応(いらないかも？))
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)

#各特定要素が表示されるまで待機
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
print('try to test')
#測定開始ボタンが表示されるまで待機
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'lv7K9c')))
#測定開始ボタンクリック
driver.find_element(By.CLASS_NAME, 'lv7K9c').click()

time.sleep(20)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'BbqFQc')))
png = driver.find_element(By.CLASS_NAME, 'fn1k4').screenshot_as_png
#スクショ保存
with open('./ss3.png', 'wb') as f:
    f.write(png)

driver.close()
driver.quit()