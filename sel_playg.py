from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://finalyze.io")

assert "Finalyze" in driver.title

comments = ["hi abhimanyu", "I am a selenium boi now", "feel the wrath of my looped finalyze iquiries", "bwa ha ha", "okay i'm done miss u bye"]



driver.find_element_by_name('submit').click()'''
