# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# driver起動
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# wait明示処理(それぞれでタイムアウト指定してるからいらない説)←やっぱりいる(try配下で使う)
driver.implicitly_wait(30)

#ページ遷移
driver.get('https://www.speedtest.net/ja')
print('pages_open')

#各特定要素が表示されるまで待機
print('try to test')
#WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'start-text')))
driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
button_elements = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
#WebDriverWait(driver, 120).until()))

#result画面に遷移する前に50 Billion tests hoge~が出たら例外処理でクリックする用←50 Billion hogeが出る前提で順番を入れ替え
#50 billion hogeが出なければ例外処理の中でスクショを保存する

#ss取るためのページサイズ変更(見切れ防止に一応(いらないかも？))
#w = driver.execute_script('return document.body.scrollWidth')
#h = driver.execute_script('return document.body.scrollHeight')
#driver.set_window_size(w, h)

try:
    WebDriverWait(driver, 240).until(EC.presence_of_all_elements_located)
    if driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button'):
        print('result pages timeout, now checking the presence of the close button, but timeout 60sec :(')
        driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button').click()
        time.sleep(1)
        png = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]').screenshot_as_png

except:
    print('??????????????')
    WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CLASS_NAME, 'pre-fold mobile-test-complete')))
    time.sleep(1)
    png = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]').screenshot_as_png

#スクショ保存
with open('./ss.png', 'wb') as f:
    f.write(png)

driver.close()
driver.quit()
