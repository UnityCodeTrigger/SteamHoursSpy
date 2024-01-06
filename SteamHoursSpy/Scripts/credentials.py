import json
profileIdExample_url = "missing url"

def GetCredentialsFromFile():
    with open('credentials.json', 'r') as archivo:
        credentials = json.load(archivo)
    
    return credentials

def GetCredentials():
    print("Steam credentials:")
    steamUser = input("Steam user: ")
    steamPass = input("Steam password: ")
    familyModePass = input("Family mode pass: \nIf is disabled type '0'\n")
    profileId = input(f"Profile id: \nExample: {profileIdExample_url}\n")
    goto = input(f"Goto: \nIf 'profileId' is not empty you can skip with ENTER.")
    
    print()
    print("Whatsapp credentials:")
    contactName = input("Contact/Group name: ")
    
    credentials = {"steamUser" : steamUser, "steamPass" : steamPass, "familyModePass" : familyModePass, "profileId" : profileId, "goto" : goto, "contactName" : contactName}
    return credentials