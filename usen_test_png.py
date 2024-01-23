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
driver.get('https://speedtest.gate02.ne.jp/')
print('pages_open')

#ss取るためのページサイズ変更(見切れ防止に一応(いらないかも？))
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)

#各特定要素が表示されるまで待機
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
print('try to test')
#WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '測定開始')))
#測定開始ボタンクリック
driver.execute_script('javascript:speedtest.start();')
time.sleep(20)

png = driver.find_element(By.CLASS_NAME, 'speedtest_content').screenshot_as_png
#スクショ保存
with open('./ss2.png', 'wb') as f:
    f.write(png)

driver.close()
driver.quit()