from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

harf=str(input("Hangi harfi aramak istersiniz? "))
time.sleep(2)
class Checking:

    def checkLetters():
        toplam=0
        driver = webdriver.Chrome(options=options)
        driver.get("https://travelcomic.com/81-2/")
        time.sleep(1)
        scrolls = 3
        for _ in range(scrolls):
            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)
        cities = driver.find_elements(By.CSS_SELECTOR, "div.uncode_text_column p span")
        time.sleep(1)
        for city in cities:
            print(city.text)
            if harf in (str(city.text)).lower():
                print("Harf bulundu+1")
                toplam+=1         
        print(f"{harf} harfi {toplam} adet şehirde bulunur! ")
        time.sleep(1)
        driver.close()

if type(harf)==str and len(harf)==1:
    Checking.checkLetters()
else:
    raise Exception("Lütfen geçerli bir değer giriniz! ")
