#video-title

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # usb 관련 에러 뜨는거 안뜨게 하기 위한 옵션인듯
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url='https://www.youtube.com/@aiacademy131/videos') # 유투브 채널 주소
time.sleep(3)

for i in range(0,5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

titles = driver.find_elements(By.CSS_SELECTOR, '#video-title-link')
print(titles)



from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet('오토코더')
wb.remove_sheet(wb['Sheet'])
ws.append(['제목', '주소'])

for title in titles:
    print(title.get_attribute('title'), title.get_attribute('href'))
    ws.append([title.get_attribute('title'), title.get_attribute('href')])

wb.save('./230407_@aiacademy131.xlsx') # 저장할 엑셀 파일의 폴더 경로 및 이름