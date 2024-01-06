import time
from Scripts import steam, whatsapp, credentials

respose = input("Load credentials from credentials.json? [y/n]")
if(respose == "y"):
    data = credentials.GetCredentialsFromFile()
elif (respose == "n"):
    data = credentials.GetCredentials()


steam.SetupDriver(steamUser=data["steamUser"], steamPass= data["steamPass"], profileId= data["profileId"], familyModePass= data["familyModePass"], goto= data["goto"])
whatsapp.SetupWhatsapp(contactName=data["contactName"])

i = 30
while(i > 0):
    msg = steam.GetHours()
    whatsapp.SendMessage(msg)
    i -= 1
    time.sleep(60 * 5)