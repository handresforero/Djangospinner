import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

#sudo chmod -R 777 /path/to/gecko
#import os;path = os.getenv('PATH'); print(path);
#/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
#sudo apt install chromium-browser # install chronium 

PATH = "/home/aforero/parseURL_Elnoti/chromedriver" #Modificar cuando se cambie de compu
#driver = webdriver.Chrome(PATH)
#/home/aforero/parseURL_Elnoti

from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('/home/aforero/chromedriver',chrome_options=chrome_options)

driver = webdriver.Chrome(PATH)
#driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get("https://aiarticlespinner.co/es/cambiador-de-palabras")


driver.find_element_by_xpath("/html/body/div[1]/main/article/content/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/span/span[1]/span/span[1]").click()
driver.find_element_by_class_name("select2-search__field").send_keys("Spanish")
driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html/body/div[1]/main/article/content/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/span/span[1]/span/span[1]").click()
driver.find_element_by_class_name("select2-search__field").send_keys("Spanish")
driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)

driver.find_element_by_xpath("/html/body/div[1]/main/article/content/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/textarea").send_keys("Esto es una prueba que quiero que me salga lo más rápido posible")
driver.find_element_by_id("submit-spinner").click()

driver.find_element_by_id("out").text
time.sleep(10)
contents = driver.find_element_by_id('out').get_attribute('value')
print(contents)



