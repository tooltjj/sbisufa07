from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://yandex.ru/" #открыть проверяемый адрес
driver = webdriver.Chrome(executable_path="C:/Users/Ansid/PycharmProjects/pythonProject/venv/chromedriver/chromedriver.exe")
driver.get("https://yandex.ru/")
elem = driver.find_element(By.ID, "text")
print(elem) #проверка, что элемент "Поиск" на данной странице найден
elem.send_keys('Тензор') #проверка ввода искомого слова\фразы
time.sleep(10)
sug_elem = driver.find_elements(By.ID,"")

try:
    driver.get(url = url)
    driver.get_screenshot_as_file("1.png")
    driver.save_screenshot("2.png")

    time.sleep(5)

finally:
    driver.close()
    driver.quit()
