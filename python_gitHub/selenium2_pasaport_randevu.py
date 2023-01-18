import time
from PIL import Image
import pytesseract

from selenium import webdriver
from selenium.webdriver.common.by import By

surucu = webdriver.Firefox()
surucu.get("https://randevu.nvi.gov.tr/")
assert "Randevu" in surucu.title

elements = surucu.find_elements(By.CLASS_NAME,"fs10")
for e in elements:
    if(e.text == "PASAPORT"):
        e.click()
        print("pasaporta tıklanma gerçekleşti")
        break
time.sleep(2)
surucu.find_element(By.XPATH,"//*[contains(text(), 'Kabul Ediyorum')]").click()
print("Kabul Ediyorum a tıklanma gerçekleti")
time.sleep(15)
surucu.find_element(By.XPATH, '//*[@id="pasaport"]/div/div/div/div[3]/div/button').click()
print("Seç e  Tıklanma gerçekleşti")
adiniz = surucu.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/form/div[2]/div[1]/div[1]/div/input')
adiniz.send_keys("SEYFETTİN")
print("Ad yazıldı")
captcha = surucu.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/form/div[2]/div[1]/div[6]/div/div/img')
with open('captcha.png', 'wb') as f:
    f.write(captcha.screenshot_as_png)
time.sleep(1)
captcha = pytesseract.image_to_string(Image.open('captcha.png'))
sekilli = surucu.find_element(By.XPATH, '//*[@id="divKisi"]/div[1]/div[6]/div/input')
sekilli.send_keys(captcha)
print("Captcha:", captcha)
print("Captcha Yazıldı")
