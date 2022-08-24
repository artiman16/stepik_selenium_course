from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    go = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    go.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element(By.ID, "input_value").text
    
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
