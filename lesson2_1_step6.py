from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
        
    
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    pic = browser.find_element(By.TAG_NAME, "img")
    att = pic.get_attribute("valuex")
    
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    
    x = att
    y = calc(x)
   
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
