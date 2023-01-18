from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

surucu=webdriver.Chrome()
surucu.get("http://www.python.org")
assert "Python" in surucu.title
element=surucu.find_element(By.NAME,"q")
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)
assert  "Yanıt bulunamadı" not in surucu.page_source

#surucu.close()