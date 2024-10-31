from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# selenium은 web페이지에서 데이터를 가져오기 위한 라이브러리

url = 'https://www.google.co.kr/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb') #엘리먼트 찾기
search_box.send_keys("KBO 한국시리즈") # 마우스, 키보드 입력
search_box.send_keys(Keys.RETURN)
time.sleep(20)