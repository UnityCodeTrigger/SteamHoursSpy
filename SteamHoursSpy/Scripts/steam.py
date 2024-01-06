# Get into Steam
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def SetupDriver(steamUser,steamPass,profileId, familyModePass = 0, goto = ""):

    global driver
    
    service = webdriver.ChromeService('.\Selenium\chromedriver.exe')
    driver = webdriver.Chrome(service = service)

    user = steamUser
    password = steamPass
    famlilyPass = familyModePass

    if(goto == ""):
        driver.get(f"https://steamcommunity.com/login/home/?goto=id/{profileId}")
    else:
        driver.get(f"https://steamcommunity.com/login/home/?goto={goto}")

    time.sleep(1)

    input_user = driver.find_element(By.XPATH, '//input[@type="text" and @class="newlogindialog_TextInput_2eKVn"]')
    input_user.send_keys(user)
    input_pass = driver.find_element(By.XPATH, '//input[@type="password" and @class="newlogindialog_TextInput_2eKVn"]')
    input_pass.send_keys(password)

    input_button = driver.find_element(By.XPATH, '//button[@type="submit" and @class="newlogindialog_SubmitButton_2QgFE"]')
    input_button.click()

    time.sleep(5)

    if(familyModePass != 0):
        input_parental = driver.find_element(By.XPATH, '//input[@type="password"]')
        input_parental.send_keys(famlilyPass)

    input_parentalbutton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    input_parentalbutton.click()
    
def GetHours():
    driver.refresh()
    time.sleep(3)
    timePlayed = driver.find_element(By.XPATH, '//div[@class="recentgame_quicklinks recentgame_recentplaytime"]/h2')
    return timePlayed.text
