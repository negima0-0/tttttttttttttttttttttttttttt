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
driver.get('https://www.speedtest.net/ja')
print('pages_open')

#ss取るためのページサイズ変更(見切れ防止に一応(いらないかも？))
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)

#各特定要素が表示されるまで待機
print('try to test')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'start-text')))
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
button_elements = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')

#result画面に遷移する前の50 Billion tests hoge~が出てきたときのクリック用
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'pre-fold mobile-test-complete')))
    time.sleep(1)
    png = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]').screenshot_as_png
except:
    print('result pages timeout, now checking the presence of the close button, but timeout 60sec')
    if driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button'):
        driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button').click()
        time.sleep(1)
        png = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]').screenshot_as_png

#スクショ保存
with open('./ss.png', 'wb') as f:
    f.write(png)

driver.close()
driver.quit()
