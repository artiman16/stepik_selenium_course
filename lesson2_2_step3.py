from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    sum = str(int(num1.text)+int(num2.text))
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum) # ищем элемент с текстом "Python"    
   
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
