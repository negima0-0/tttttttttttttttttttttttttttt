#UTF-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# driver起動
driver = webdriver.Chrome()

# wait明示処理
driver.implicitly_wait(30)
#ページ遷移
driver.get('https://www.speedtest.net/ja')

#ss取るためのページサイズ変更(見切れ防止に一応)
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)

#特定要素が表示されるまで待機
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'start-text')))
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'audience-survey audience-survey-type-nps')))
    time.sleep(1)
    png = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]').screenshot_as_png

    with open('./ss.png', 'wb') as f:
        f.write(png)
except Exception as e:
    print(e)
    print('detect error')

driver.close()
driver.quit()
