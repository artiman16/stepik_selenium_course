from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 14).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    button = browser.find_element(By.ID, "book")
    button.click()
    
    x = browser.find_element(By.ID, "input_value").text
    
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    solve = browser.find_element(By.ID, "solve")
    solve.click()
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
