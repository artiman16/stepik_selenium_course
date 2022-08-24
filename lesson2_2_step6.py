from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.ID, "input_value").text
    
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    browser.execute_script("window.scrollBy(0, 100);")
   
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check.click()
    
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
      
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
