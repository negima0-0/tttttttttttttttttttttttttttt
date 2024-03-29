from os import pipe
import time
from socket import timeout # it is used to connect a client and a server
from selenium import webdriver # the holy webdriver to control all all the commands
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome() #storing the webdriver in a variable
url = "https://fast.com/"
driver.get(url) #this time its an custom made website to test web threats.
print("\n\n")
wait = WebDriverWait(driver, 60)
try:
    infoLink = wait.until(
            EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[2]/div[1]/div[4]/div[1]/a'))
            )
    status = infoLink.is_displayed()
    if(status ==  True):
        #the speed values be it in 100 or thousands
        speedvalue = wait.until(
            EC.presence_of_element_located(
            (By.ID, 'speed-value'))
            )
        #for the speed test units be it in mpbs or kbps acc. to the browser
        speedunits = wait.until(
            EC.presence_of_element_located(
            (By.ID, 'speed-units'))
            )
        png = driver.find_element(By.XPATH,'/html/body/div').screenshot_as_png
        with open('./fastcom.png', 'wb') as f:
            f.write(png)
        print(speedvalue.text, speedunits.text) #debug
        driver.execute_script("window.open('https://google.com')") #test open new tab
        time.sleep(5)
    driver.quit()
except :
    print("You have problem with internet connection. (fast.com)")
    driver.quit()
