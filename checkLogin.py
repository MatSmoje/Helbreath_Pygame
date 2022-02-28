import pygame
import json

class BbddLogin():
    def __init__(self):
        pass
    
    def checkCredentials(self, user, passwd):
        accFolder = 'S_Data/S_'+user+'/'
        accFile = 'A_'+user+'.json'
        try:
            with open(accFolder+accFile, "r") as jsonFile:
                jsonObject = json.load(jsonFile)
                jsonFile.close()
                print(jsonObject)
            usr = jsonObject['NAME']['account-name']
            pwd = jsonObject['PASSWORD']['account-password']

            if user == usr and passwd == pwd:
                return True
        except:
            return False

    def register(self):
        # create new folder with information of account
        pass

    def createAccount(self):
        # create file in folder with pj information
        pass


test = BbddLogin()
test.checkCredentials('anton','b')