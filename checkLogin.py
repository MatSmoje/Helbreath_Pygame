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

    def addToPJList(self, characterName):
        accFolder = 'S_Data/CharacterList.txt'
        with open(accFolder, "a+") as charList:
            charList.write("\n")
            charList.write(characterName)
            charList.close()

    def writeIntoAccFile(self, user, charcterName):
        accFolder = 'S_Data/S_'+ user + '/A_' + user +'.json'
        print(accFolder)
        with open(accFolder) as fp:
            listObj = json.load(fp)
        
            if len(listObj["CHARACTERS"]["account-character"])<=3:
                listObj["CHARACTERS"]["account-character"].append(charcterName)
                with open(accFolder, "w") as jsonFile:
                    json.dump(listObj, jsonFile, indent=4,  separators=(',',': '))
                return True
            else:
                print("Supera el máximo de PJ")
                return False
            
        

        #acc["CHARACTERS"]["account-character"].append(charcterName)
        


    def checkExistenceOfPj(self, characterName):
        accFolder = 'S_Data/CharacterList.txt'
   
        with open(accFolder, "r") as chars:
            charList = chars.read()
            chars.close()
        if characterName in charList:
            return True
        else:
            return False



# test = BbddLogin()
# test.writeIntoAccFile('anton','Kanazawa')