from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def SetupWhatsapp(contactName):
    global driver
    
    service = webdriver.ChromeService('.\Selenium\chromedriver.exe')
    driver = webdriver.Chrome(service = service)
    
    driver.get("https://web.whatsapp.com/")
    
    respose = input("Has escaneado y se han cargado los chats? [y/n]")
    
    if(respose != "y"):
        return
    
    chat = driver.find_element(By.XPATH, f'//span[text()="{contactName}"]')
    chat.click()
    
    time.sleep(1)
    
    global msgContainer
    msgContainer = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    
        
def SendMessage(msg):
    msgContainer = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    msgContainer.click()
    msgContainer.send_keys(msg)
    sendButton = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    sendButton.click()
    print(f"Message sended\nmessage:'{msg}'")