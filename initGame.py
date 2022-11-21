from itertools import count
import pygame
import testHbPak
from PIL import Image
from pygame.locals import *
import json
import lan_eng, textInput
import time



class StartGame(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.totalSprites = { }
        self.MakeSprite("New-Dialog.pak")
        self.MakeSprite("interface.pak")
        self.m_cLoading = 4
        self.startGameVar = 0
        self.passwordState = False
        self.accountState = False
        self.msg = textInput.inputText(0 , 0 , self.screen)
        self.exitTrigger = False
        self.charSelection = 0
        self.user = ''
        self.index  = 0
        self.warp_at_time = 0
        ### stats
        self.specialStatPoints = 10 
        self.str = 10 
        self.vit = 10 
        self.dex = 10 
        self.int = 10 
        self.mag = 10 
        self.chr = 10 

    def printSprites(self, totalSprites):
        print(json.dumps(totalSprites, sort_keys=True, indent=2, default=str))

    def resetValues(self):
        self.specialStatPoints = 10 
        self.str = 10 
        self.vit = 10 
        self.dex = 10 
        self.int = 10 
        self.mag = 10 
        self.chr = 10
    
    def update(self, spriteObj, n, posX, posY ):
        NOW_MS = int(time.time() * 1000.0)
        spriteLen = len(spriteObj["sprites"])
        frameLen = len(spriteObj["frames"][n])
        refreshTime = 1000 // frameLen
        print(spriteLen)
        print(frameLen)
        
        
        
        if self.index >= frameLen:
            self.index = 0
        self.screen.blit(spriteObj["sprites"][n], (posX,posY), spriteObj["frames"][n][self.index][0:4])


        # if (self.warp_at_time > 0):
        #     ms_since_warp_start = NOW_MS - self.warp_at_time
        #     if ( ms_since_warp_start > 1000 ):
        #         self.warp_at_time = 0
        #         self.image = sprite  # return to original bitmap
               
        #     else:
        #         image_number = ms_since_warp_start // 125 
        #         self.image = sprite[image_number] # show that image
        # return self.image

########################################################## GAME STATES  ####################################################################

    def startGame(self):
        warp_at_time = 0
        loading = self.totalSprites["New-Dialog.pak"]["sprites"][0]
        newAcc = self.totalSprites["New-Dialog.pak"]["sprites"][1]
        exit = self.totalSprites["New-Dialog.pak"]["sprites"][2]
        
        if self.m_cLoading == 100:
            logIn = self.totalSprites["LoginDialog.pak"]["sprites"][0]
            gameDialog = self.totalSprites["GameDialog.pak"]["sprites"][8]


##################### LOGIN - NEW ACC - EXIT #######################
        if self.startGameVar == 0 and self.m_cLoading < 100: 
            rect = loading.get_rect()
            self.screen.blit(loading, rect)
            self.UpdateScreen_OnLoading()
            print(self.m_cLoading)
        
        if self.startGameVar == 0 and self.m_cLoading == 100:
            rect = newAcc.get_rect()
            self.screen.blit(newAcc, rect)
            login = pygame.Rect((386, 179), (162, 20))
            newAccount = pygame.Rect((386, 217), (162, 20))
            exit = pygame.Rect((386, 256), (162, 20))

            if login.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(newAcc,(386, 179),(134, 484, 162, 20)) 
                return 1 #Login

            if newAccount.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(newAcc,(386, 217),(301, 484, 162, 20))
                return 2 # New Account

            if exit.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(newAcc,(386, 256),(468, 484, 162, 20))
                return 99 # Exit
##################### CHOOSE SERVER ABBY - APOC  #######################

        if self.startGameVar == 1:                              # Login
            rect = logIn.get_rect()
            self.screen.blit(logIn, rect)
            self.screen.blit(logIn, (40,120), self.totalSprites["LoginDialog.pak"]["frames"][0][1][0:4])
            
            if pygame.Rect((256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][2:4]).collidepoint(pygame.mouse.get_pos()):
            # Cancel
                self.screen.blit(logIn, (256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][0:4])
                return 3
            # Abadon Server
            if pygame.Rect((139, 175), self.totalSprites["LoginDialog.pak"]["frames"][0][5][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(logIn, (139,175), self.totalSprites["LoginDialog.pak"]["frames"][0][5][0:4])
                return 4
            # Apocalipsis Server
            if pygame.Rect((130, 205), self.totalSprites["LoginDialog.pak"]["frames"][0][6][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(logIn, (130,205), self.totalSprites["LoginDialog.pak"]["frames"][0][6][0:4])
                return 5
            
            #self.screen.blit(image1, self.totalSprites["LoginDialog.pak"]["frames"][0][0])
        

##################### LOGIN- ACC - PASSWORD #######################
        if self.startGameVar == 2:
            # Limpiar datos

            rect = logIn.get_rect()
            self.screen.blit(logIn, rect)
            
            self.screen.blit(logIn, (40,120), self.totalSprites["LoginDialog.pak"]["frames"][0][2][0:4])
            if pygame.Rect((256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][2:4]).collidepoint(pygame.mouse.get_pos()):
            # Cancel
                self.screen.blit(logIn, (256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][0:4])
                print("State 6")
                return 6
            # Connect
            if pygame.Rect((82,282), self.totalSprites["LoginDialog.pak"]["frames"][0][3][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(logIn, (82,282), self.totalSprites["LoginDialog.pak"]["frames"][0][3][0:4])
                return 7
            
            # Account Box
            if pygame.Rect((176,162),(147,18)).collidepoint(pygame.mouse.get_pos()):              
                return 8
            
            # Passwd Box
            if pygame.Rect((176,185),(147,18) ).collidepoint(pygame.mouse.get_pos()):
                return 9

######################## LOGEADO - CHOOSE CHARACTER 
       

        if self.startGameVar == 3:  
            rect = gameDialog.get_rect()
            self.screen.blit(gameDialog, rect)
            

            ###LOGICA GET CHARS###
            
            


            ###LOGICA GET CHARS###

            self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER36, 137, 452)
            charSelectionList = [(103,54),(212,54),(321,54),(430,54)]
            self.dialogText1.set_colorkey((0,123,255))
            self.screen.blit(self.dialogText1, charSelectionList[self.charSelection], self.totalSprites["DialogText.pak"]["frames"][1][62][0:4])

            accFolder = 'S_Data/S_'+ self.user +'/A_' + self.user + '.json'
            with open(accFolder, "r") as accFile:
                accInfo = accFile.read()
                accFile.close()

            accInfo = json.loads(accInfo)
            listOfCharacters = accInfo["CHARACTERS"]["account-character"]
            characterCoord = [[115,177,145,193,145,208],[225,177,265,193,265,208],[335,177,365,193,365,208],[445,177,475,193,475,208]]
            pjCoord = [142,252,362,472]
            counter = 0 
            for character in listOfCharacters:
                charJSONFile = 'S_Data/S_'+ self.user +'/C_' + character + '.json'
                with open(charJSONFile, "r") as jsonFile:
                    char = jsonFile.read()
                    jsonFile.close()
                y = json.loads(char)
                self.msg.writeText(y["NAME-ACCOUNT"]["character-name"], characterCoord[counter][0], characterCoord[counter][1])
                self.msg.writeText(str(y["STATUS"]["character-LEVEL"]), characterCoord[counter][2], characterCoord[counter][3])
                self.msg.writeText(str(y["STATUS"]["character-EXP"]), characterCoord[counter][4], characterCoord[counter][5])
                #16 a 23
                #self.update(self.totalSprites["Wm.pak"],16, 142, 195)#[0][0:4]))
                image_number = 0
                NOW_MS = int(time.time() * 1000.0) #21.000

                if (self.warp_at_time == 0):
                    self.warp_at_time = NOW_MS #20.000


                ms_since_warp_start = NOW_MS - self.warp_at_time #1.000

                if ( ms_since_warp_start > 125*7 ):
                    self.warp_at_time = 0
                else:
                    image_number = ms_since_warp_start // 125
                    print("image number" + str(image_number))
                
                self.totalSprites["Wm.pak"]["sprites"][16].set_colorkey((0,0,0))
                self.totalSprites["Bm.pak"]["sprites"][16].set_colorkey((0,0,0))
                self.totalSprites["Ym.pak"]["sprites"][16].set_colorkey((0,0,0))


                if(y["STATUS"]["skin-status"] == 1):
                    self.screen.blit(self.totalSprites["Wm.pak"]["sprites"][16], (pjCoord[counter],95), self.totalSprites["Wm.pak"]["frames"][16][image_number][0:4])
                if(y["STATUS"]["skin-status"] == 2):
                    self.screen.blit(self.totalSprites["Bm.pak"]["sprites"][16], (pjCoord[counter],95), self.totalSprites["Bm.pak"]["frames"][16][image_number][0:4])
                if(y["STATUS"]["skin-status"] == 3):
                    self.screen.blit(self.totalSprites["Ym.pak"]["sprites"][16], (pjCoord[counter],95), self.totalSprites["Ym.pak"]["frames"][16][image_number][0:4])
                counter = counter + 1 

            
            

            if pygame.Rect((106,57),(100,180)).collidepoint(pygame.mouse.get_pos()):   ### print("Character Box1")
                return 10 

            if pygame.Rect((216,57),(100,180)).collidepoint(pygame.mouse.get_pos()):
                return 11
            
            if pygame.Rect((327,57),(100,180)).collidepoint(pygame.mouse.get_pos()):
                return 12

            if pygame.Rect((433,57),(100,180)).collidepoint(pygame.mouse.get_pos()):    ### print("Character Box4")
                return 13
            
            if pygame.Rect((365,288),(176,22)).collidepoint(pygame.mouse.get_pos()):          ### print("Start Box")
                self.screen.blit(self.dialogText1, (365,288), self.totalSprites["DialogText.pak"]["frames"][1][56][0:4])
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER1, 105, 285 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER2, 105, 300 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER3, 105, 315 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER4, 105, 330 )
                return 14
            
            if pygame.Rect((365,318),(176,22)).collidepoint(pygame.mouse.get_pos()):           #### print("NewChar Box")
                self.screen.blit(self.dialogText1, (365,318), self.totalSprites["DialogText.pak"]["frames"][1][57][0:4])
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER5, 105, 310 )
                return 15
            
            if pygame.Rect((365,348),(176,22)).collidepoint(pygame.mouse.get_pos()):           #### print("DeleteChar Box")
                self.screen.blit(self.dialogText1, (365,348), self.totalSprites["DialogText.pak"]["frames"][1][58][0:4]) #check
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER6, 105, 285 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER7, 105, 300 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER8, 105, 315 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER9, 105, 330 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER10, 105, 345 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER11, 105, 360 )
                return 16

            if pygame.Rect((365,378),(176,22)).collidepoint(pygame.mouse.get_pos()):           #### print("Change Password")
                self.screen.blit(self.dialogText1, (365,378), self.totalSprites["DialogText.pak"]["frames"][1][59][0:4]) #check
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER12, 105, 310 )
                return 17
            
            if pygame.Rect((365,408),(176,22)).collidepoint(pygame.mouse.get_pos()):               ### print("LogoutBox")
                self.screen.blit(self.dialogText1, (365,408), self.totalSprites["DialogText.pak"]["frames"][1][60][0:4]) #check
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER13, 105, 310)
                return 18
            
            

        
######################## CREATE NEW CHARACTER
        if self.startGameVar == 4:
            gameDialog = self.totalSprites["GameDialog.pak"]["sprites"][9]
            
            
            rect = gameDialog.get_rect()
            self.screen.blit(gameDialog, rect)
            

            self.itemEquipM0.set_colorkey((0,0,0))
            self.screen.blit(self.itemEquipM0, (376,100),self.totalSprites["item-equipM.pak"]["frames"][0][1][0:4])
            #.set_colorkey(0,123,255)


            
            self.screen.blit(self.dialogText1, (375,448), self.totalSprites["DialogText.pak"]["frames"][1][24][0:4])
            self.screen.blit(self.dialogText1, (505,448), self.totalSprites["DialogText.pak"]["frames"][1][16][0:4]) #Cancel

            self.screen.blit(self.dialogText1, (59,448), self.totalSprites["DialogText.pak"]["frames"][1][67][0:4])  # WARRIOR
            self.screen.blit(self.dialogText1, (144,448), self.totalSprites["DialogText.pak"]["frames"][1][65][0:4]) # MAGE
            self.screen.blit(self.dialogText1, (229,448), self.totalSprites["DialogText.pak"]["frames"][1][63][0:4]) # MASTER
            

            #56 start 
            self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER1, 95, 85)
            self.msg.writeText(lan_eng.MSG_CHARACTERNAME, 77, 106)
            self.msg.writeText(lan_eng.MSG_GENDER, 77, 155)
            self.msg.writeText(lan_eng.MSG_SKINCOLOR, 77, 172)
            self.msg.writeText(lan_eng.MSG_HAIRSTYLE, 77, 187)
            self.msg.writeText(lan_eng.MSG_HAIRCOLOR, 77, 202)
            self.msg.writeText(lan_eng.MSG_UNDERWEARCOLOR, 77, 217)

            self.msg.writeText(lan_eng._BDRAW_ON_CREATE_NEW_CHARACTER4+" "+ str(self.specialStatPoints), 95, 249)

            self.msg.writeText(lan_eng.MSG_STRENGTH, 77, 270)
            self.msg.writeText(lan_eng.MSG_VITALITY, 77, 286)
            self.msg.writeText(lan_eng.MSG_DEXTERITY, 77, 302)
            self.msg.writeText(lan_eng.MSG_INTELLIGENCE, 77, 318)
            self.msg.writeText(lan_eng.MSG_MAGIC, 77, 334)
            self.msg.writeText(lan_eng.MSG_CHARSIMA, 77, 350)

            self.msg.writeText(lan_eng.MSG_HITPOINT, 440, 187)
            self.msg.writeText(lan_eng.MSG_MANAPOINT, 440, 203)
            self.msg.writeText(lan_eng.MSG_STAMINARPOINT, 440, 220)
        


            ## TEST NUMBER WRITE
            # hitPoint = 
            manaPoint =  2* self.mag + 0.5 * self.int
            staminarPoint = 2 + 2 * self.str
            self.msg.writeText("37", 550, 190)
            self.msg.writeText(str(manaPoint), 550, 205)
            self.msg.writeText(str(staminarPoint), 550, 220)

            self.msg.writeText(str(self.str), 203, 275) # STR
            self.msg.writeText(str(self.vit), 203, 290) # VIT
            self.msg.writeText(str(self.dex), 203, 305) # DEX
            self.msg.writeText(str(self.int), 203, 323) # INT
            self.msg.writeText(str(self.mag), 203, 338) # MAG
            self.msg.writeText(str(self.chr), 203, 353) # CHR



            if pygame.Rect((505,448),(75,19)).collidepoint(pygame.mouse.get_pos()):   # Cancel BTN
                self.screen.blit(self.dialogText1, (505,448), self.totalSprites["DialogText.pak"]["frames"][1][17][0:4])
                return 19

            if pygame.Rect((375,448),(75,19)).collidepoint(pygame.mouse.get_pos()):   # CREATE BTN
                self.screen.blit(self.dialogText1, (375,448), self.totalSprites["DialogText.pak"]["frames"][1][25][0:4])
                return 20

            # MOUSEHOVER OVER  STR
            if pygame.Rect((236,276),(21,15)).collidepoint(pygame.mouse.get_pos()): # + STR
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 21
            if pygame.Rect((258,276),(21,15)).collidepoint(pygame.mouse.get_pos()): # - STR
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 22
            if pygame.Rect((236,294),(21,15)).collidepoint(pygame.mouse.get_pos()): # + VIT
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 23
            if pygame.Rect((258,294),(21,15)).collidepoint(pygame.mouse.get_pos()): # - VIT
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 24
                                
            if pygame.Rect((236,312),(21,13)).collidepoint(pygame.mouse.get_pos()): # + DEX
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 25

            if pygame.Rect((258,312),(21,13)).collidepoint(pygame.mouse.get_pos()): # - DEX
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 26
                                                
            if pygame.Rect((236,328),(21,14)).collidepoint(pygame.mouse.get_pos()): # + INT
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 27

            if pygame.Rect((258,328),(21,14)).collidepoint(pygame.mouse.get_pos()): # - INT
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 28

            if pygame.Rect((236,342),(21,15)).collidepoint(pygame.mouse.get_pos()): # + MAG
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 29

            if pygame.Rect((258,342),(21,15)).collidepoint(pygame.mouse.get_pos()): # - MAG
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 30
            
            if pygame.Rect((236,358),(21,14)).collidepoint(pygame.mouse.get_pos()): # + CHR
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                # self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 31
                
            if pygame.Rect((258,357),(21,15)).collidepoint(pygame.mouse.get_pos()): # - CHR
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
                return 32

            if pygame.Rect((59,448),(75,19)).collidepoint(pygame.mouse.get_pos()):   # CREATE WARRIOR
                self.screen.blit(self.dialogText1, (59,448), self.totalSprites["DialogText.pak"]["frames"][1][68][0:4])
                return 33
                

            if pygame.Rect((144,448),(75,19)).collidepoint(pygame.mouse.get_pos()):   # CREATE MAGE
                self.screen.blit(self.dialogText1, (144,448), self.totalSprites["DialogText.pak"]["frames"][1][66][0:4])
                return 34
                
            if pygame.Rect((229,448),(75,19)).collidepoint(pygame.mouse.get_pos()):   # CREATE MASTER
                self.screen.blit(self.dialogText1, (229,448), self.totalSprites["DialogText.pak"]["frames"][1][64][0:4])
                return 35
            
            if pygame.Rect((195,110),(105,15)).collidepoint(pygame.mouse.get_pos()): # Write Char Name
                print("WriteChar")
                return 36
           
            



            
        

            
        
            

######################### Exit

        if self.startGameVar == 99:
            self.exitTrigger = True                             
            rect = exit.get_rect()
            self.screen.blit(exit, rect)
            self.screen.blit(exit, (255,122), self.totalSprites["New-Dialog.pak"]["frames"][2][1][0:4])
            
            
            
            

########################################################## GAME STATES  ####################################################################
    def Login(self):
        logIn = self.totalSprites["LoginDialog.pak"]["sprites"][0]
        rect = logIn.get_rect()
        self.screen.blit(logIn, rect)

    def cursor(self): #32 x 27
        cursor = self.totalSprites["interface.pak"]["sprites"][0]
        surf = pygame.Surface((32, 27)) # you could also load an image 
        cursor.set_colorkey((255,132,66))
        surf.set_colorkey((0,0,0))
        surf.blit(cursor,(0,0),(121, 6, 32, 27))
        color = pygame.cursors.Cursor((5, 5), surf)
        pygame.mouse.set_cursor(color)

    def MakeSprite(self, file):
        path = "Sprites/"
        p_Sprite = testHbPak.HBPak(path + file)
        spriteInfo =  p_Sprite.load()
        self.totalSprites[next(iter(spriteInfo))] = spriteInfo[next(iter(spriteInfo))]
        self.printSprites(self.totalSprites)
        return self.totalSprites        

    def UpdateScreen_OnLoading(self):
        if self.m_cLoading == 0:
            print("Posible Error")
            self.m_cLoading = 4
        elif self.m_cLoading == 4:
            self.MakeSprite('LoginDialog.pak')
            self.MakeSprite('GameDialog.pak')
            self.MakeSprite('DialogText.pak')
            self.dialogText0 = self.totalSprites["DialogText.pak"]["sprites"][0]
            self.dialogText1 = self.totalSprites["DialogText.pak"]["sprites"][1]
            self.MakeSprite('item-equipM.pak')
            self.itemEquipM0 = self.totalSprites["item-equipM.pak"]["sprites"][0]
            self.itemEquipM1 = self.totalSprites["item-equipM.pak"]["sprites"][1]
            self.itemEquipM2 = self.totalSprites["item-equipM.pak"]["sprites"][2]
            self.itemEquipM3 = self.totalSprites["item-equipM.pak"]["sprites"][3]
            self.itemEquipM4 = self.totalSprites["item-equipM.pak"]["sprites"][4]
            self.itemEquipM5 = self.totalSprites["item-equipM.pak"]["sprites"][5]
            self.itemEquipM6 = self.totalSprites["item-equipM.pak"]["sprites"][6]
            self.itemEquipM7 = self.totalSprites["item-equipM.pak"]["sprites"][7]
            self.itemEquipM8 = self.totalSprites["item-equipM.pak"]["sprites"][8]
            self.itemEquipM9 = self.totalSprites["item-equipM.pak"]["sprites"][9]
            self.itemEquipM10 = self.totalSprites["item-equipM.pak"]["sprites"][10]
            self.itemEquipM11 = self.totalSprites["item-equipM.pak"]["sprites"][11]
            self.itemEquipM12 = self.totalSprites["item-equipM.pak"]["sprites"][12]
            self.itemEquipM13 = self.totalSprites["item-equipM.pak"]["sprites"][13]
            self.itemEquipM14 = self.totalSprites["item-equipM.pak"]["sprites"][14]
            self.MakeSprite('Wm.pak')
            self.MakeSprite('Bm.pak')
            self.MakeSprite('Ym.pak')
            #self.itemEquipM0 = self.totalSprites["Wm.pak"]["sprites"][0]

            self.m_cLoading = 8
        elif self.m_cLoading == 8:
            self.m_cLoading = 12
        elif self.m_cLoading == 12:
            self.m_cLoading = 16
        elif self.m_cLoading == 16:
            self.m_cLoading = 20
        elif self.m_cLoading == 20:
            self.m_cLoading = 24
        elif self.m_cLoading == 24:
            self.m_cLoading = 28
        elif self.m_cLoading == 28:
            self.m_cLoading = 32
        elif self.m_cLoading == 32:
            self.m_cLoading = 36
        elif self.m_cLoading == 36:
            self.m_cLoading = 40
        elif self.m_cLoading == 40:
            self.m_cLoading = 44
        elif self.m_cLoading == 44:
            self.m_cLoading = 48
        elif self.m_cLoading == 48:
            self.m_cLoading = 52
        elif self.m_cLoading == 52:
            self.m_cLoading = 56
        elif self.m_cLoading == 56:
            self.m_cLoading = 60
        elif self.m_cLoading == 60:
            self.m_cLoading = 100
        elif self.m_cLoading == 100:
            pass