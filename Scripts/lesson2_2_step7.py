from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Artem")
    
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Gerasimenko")
    
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("artiman16@mail.ru")
    
    button = browser.find_element(By.ID, "file")
    #button.click()
    
    import os 
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    button.send_keys(file_path)    
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()    
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()