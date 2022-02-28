import pygame
import testHbPak
from PIL import Image
from pygame.locals import *
import json
import lan_eng, textInput



class StartGame():
    def __init__(self, screen):
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

    def printSprites(self, totalSprites):
        print(json.dumps(totalSprites, sort_keys=True, indent=2, default=str))

########################################################## GAME STATES  ####################################################################

    def startGame(self):
        
        loading = self.totalSprites["New-Dialog.pak"]["sprites"][0]
        newAcc = self.totalSprites["New-Dialog.pak"]["sprites"][1]
        exit = self.totalSprites["New-Dialog.pak"]["sprites"][2]
        
        if self.m_cLoading == 100:
            logIn = self.totalSprites["LoginDialog.pak"]["sprites"][0]
            gameDialog = self.totalSprites["GameDialog.pak"]["sprites"][8]


##################### LOGIN - NEW ACC - EXIT #######################
        if self.startGameVar == 0 and self.m_cLoading < 100: 
            data, mode, size = self.prepareSprite(loading)
            image1 = pygame.image.fromstring(data, size, mode) 
            rect = image1.get_rect()
            self.screen.blit(image1, rect)
            self.UpdateScreen_OnLoading()
            print(self.m_cLoading)
        
        if self.startGameVar == 0 and self.m_cLoading == 100:
            data, mode, size = self.prepareSprite(newAcc)
            self.image1 = pygame.image.fromstring(data, size, mode)
            rect = self.image1.get_rect()
            self.screen.blit(self.image1, rect)
            login = pygame.Rect((386, 179), (162, 20))
            newAccount = pygame.Rect((386, 217), (162, 20))
            exit = pygame.Rect((386, 256), (162, 20))

            if login.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.image1,(386, 179),(134, 484, 162, 20)) 
                return 1 #Login

            if newAccount.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.image1,(386, 217),(301, 484, 162, 20))
                return 2 # New Account

            if exit.collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(self.image1,(386, 256),(468, 484, 162, 20))
                return 99 # Exit
##################### CHOOSE SERVER ABBY - APOC  #######################

        if self.startGameVar == 1:                              # Login
            data, mode, size = self.prepareSprite(logIn)
            image1 = pygame.image.fromstring(data, size, mode)
            rect = image1.get_rect()
            self.screen.blit(image1, rect)
           
            
            self.screen.blit(image1, (40,120), self.totalSprites["LoginDialog.pak"]["frames"][0][1][0:4])
            
            if pygame.Rect((256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][2:4]).collidepoint(pygame.mouse.get_pos()):
            # Cancel
                self.screen.blit(image1, (256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][0:4])
                return 3
            # Abadon Server
            if pygame.Rect((139, 175), self.totalSprites["LoginDialog.pak"]["frames"][0][5][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(image1, (139,175), self.totalSprites["LoginDialog.pak"]["frames"][0][5][0:4])
                return 4
            # Apocalipsis Server
            if pygame.Rect((130, 205), self.totalSprites["LoginDialog.pak"]["frames"][0][6][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(image1, (130,205), self.totalSprites["LoginDialog.pak"]["frames"][0][6][0:4])
                return 5
            
            #self.screen.blit(image1, self.totalSprites["LoginDialog.pak"]["frames"][0][0])
        

##################### LOGIN- ACC - PASSWORD #######################
        if self.startGameVar == 2:
            # Limpiar datos


            
            data, mode, size = self.prepareSprite(logIn)
            image1 = pygame.image.fromstring(data, size, mode)
            rect = image1.get_rect()
            self.screen.blit(image1, rect)
            
            self.screen.blit(image1, (40,120), self.totalSprites["LoginDialog.pak"]["frames"][0][2][0:4])
            if pygame.Rect((256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][2:4]).collidepoint(pygame.mouse.get_pos()):
            # Cancel
                self.screen.blit(image1, (256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][0:4])
                print("State 6")
                return 6
            # Connect
            if pygame.Rect((82,282), self.totalSprites["LoginDialog.pak"]["frames"][0][3][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(image1, (82,282), self.totalSprites["LoginDialog.pak"]["frames"][0][3][0:4])
                return 7
            
            # Account Box
            if pygame.Rect((176,162),(147,18)).collidepoint(pygame.mouse.get_pos()):              
                return 8
            
            # Passwd Box
            if pygame.Rect((176,185),(147,18) ).collidepoint(pygame.mouse.get_pos()):
                return 9

######################## LOGEADO - CHOOSE CHARACTER 

        if self.startGameVar == 3:  
            data, mode, size = self.prepareSprite(gameDialog)
            image1 = pygame.image.fromstring(data, size, mode)
            rect = image1.get_rect()
            self.screen.blit(image1, rect)
            color = (205,108,0,70)

            self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER36, 137, 452 )

            if pygame.Rect((106,57),(100,180)).collidepoint(pygame.mouse.get_pos()):   ### print("Character Box1")
                rect = (106,57,100,180)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                return 10 

            if pygame.Rect((216,57),(100,180)).collidepoint(pygame.mouse.get_pos()):
                rect = (216,57,100,180)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)    #### print("Character Box2")
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                
                return 11
            
            if pygame.Rect((327,57),(100,180)).collidepoint(pygame.mouse.get_pos()):
                rect = (327,57,100,180)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)    ###  print("Character Box3")
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                return 12

            if pygame.Rect((433,57),(100,180)).collidepoint(pygame.mouse.get_pos()):    ### print("Character Box4")
                rect = (433,57,100,180)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                return 13
            
            if pygame.Rect((365,288),(176,22)).collidepoint(pygame.mouse.get_pos()):          ### print("Start Box")
                rect = (365,288,176,22)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER1, 105, 285 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER2, 105, 300 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER3, 105, 315 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER4, 105, 330 )
                return 14
            
            if pygame.Rect((365,318),(176,22)).collidepoint(pygame.mouse.get_pos()):           #### print("NewChar Box")
                rect = (365,318,176,22)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER5, 105, 310 )
                return 15
            
            if pygame.Rect((365,348),(176,22)).collidepoint(pygame.mouse.get_pos()):           #### print("DeleteChar Box")
                rect = (365,348,176,22)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER6, 105, 285 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER7, 105, 300 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER8, 105, 315 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER9, 105, 330 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER10, 105, 345 )
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER11, 105, 360 )
                return 16

            if pygame.Rect((365,378),(176,22)).collidepoint(pygame.mouse.get_pos()):           #### print("Change Password")
                rect = (365,378,176,22)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER12, 105, 310 )
                return 17
            
            if pygame.Rect((365,408),(176,22)).collidepoint(pygame.mouse.get_pos()):               ### print("LogoutBox")
                rect = (365,408,176,22)
                shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
                self.screen.blit(shape_surf, rect)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_SELECT_CHARACTER13, 105, 310)
                return 18

        
######################## CREATE NEW CHARACTER
        if self.startGameVar == 4:
            gameDialog = self.totalSprites["GameDialog.pak"]["sprites"][9]
            data, mode, size = self.prepareSprite(gameDialog)
            image1 = pygame.image.fromstring(data, size, mode)
            rect = image1.get_rect()
            self.screen.blit(image1, rect)
            self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER1, 95, 85)
            self.msg.writeText(lan_eng.MSG_CHARACTERNAME, 77, 106)
            self.msg.writeText(lan_eng.MSG_GENDER, 77, 155)
            self.msg.writeText(lan_eng.MSG_SKINCOLOR, 77, 172)
            self.msg.writeText(lan_eng.MSG_HAIRSTYLE, 77, 187)
            self.msg.writeText(lan_eng.MSG_HAIRCOLOR, 77, 202)
            self.msg.writeText(lan_eng.MSG_UNDERWEARCOLOR, 77, 217)

            self.msg.writeText(lan_eng._BDRAW_ON_CREATE_NEW_CHARACTER4, 95, 249)

            self.msg.writeText(lan_eng.MSG_STRENGTH, 77, 270)
            self.msg.writeText(lan_eng.MSG_VITALITY, 77, 286)
            self.msg.writeText(lan_eng.MSG_DEXTERITY, 77, 302)
            self.msg.writeText(lan_eng.MSG_INTELLIGENCE, 77, 318)
            self.msg.writeText(lan_eng.MSG_MAGIC, 77, 334)
            self.msg.writeText(lan_eng.MSG_CHARSIMA, 77, 350)

            self.msg.writeText(lan_eng.MSG_HITPOINT, 440, 187)
            self.msg.writeText(lan_eng.MSG_MANAPOINT, 440, 203)
            self.msg.writeText(lan_eng.MSG_STAMINARPOINT, 440, 220)

            # MOUSEHOVER OVER  STR
            if pygame.Rect((236,276),(21,15)).collidepoint(pygame.mouse.get_pos()): # + STR
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)
            if pygame.Rect((258,276),(21,15)).collidepoint(pygame.mouse.get_pos()): # + STR
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER7, 376, 322)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER8, 376, 337)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER9, 376, 352)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER10, 376, 367)
                self.msg.writeText(lan_eng.UPDATE_SCREEN_ON_CREATE_NEW_CHARACTER11, 376, 382)

           
            



            
        

            
        
            

######################### Exit

        if self.startGameVar == 99:
            self.exitTrigger = True                             
            data, mode, size = self.prepareSprite(exit)
            image1 = pygame.image.fromstring(data, size, mode)
            rect = image1.get_rect()
            self.screen.blit(image1, rect)
            self.screen.blit(image1, (255,122), self.totalSprites["New-Dialog.pak"]["frames"][2][1][0:4])
            
            
            
            

########################################################## GAME STATES  ####################################################################
    def Login(self):
        logIn = self.totalSprites["LoginDialog.pak"]["sprites"][0]
        data, mode, size = self.prepareSprite(logIn)
        image1 = pygame.image.fromstring(data, size, mode)
        rect = image1.get_rect()
        self.screen.blit(image1, rect)

    def cursor(self): #32 x 27
        cursor = self.totalSprites["interface.pak"]["sprites"][0]
        data, mode, size = self.prepareSprite(cursor)
        surf = pygame.Surface((32, 27)) # you could also load an image 
        image1 = pygame.image.fromstring(data, size, mode)
        image1.set_colorkey((255,132,66))
        surf.set_colorkey((0,0,0))
        surf.blit(image1,(0,0),(121, 6, 32, 27))
        color = pygame.cursors.Cursor((5, 5), surf)
        pygame.mouse.set_cursor(color)
        
    def prepareSprite(self, imagen):
        data = imagen.tobytes()
        mode = imagen.mode
        size = imagen.size
        return data, mode, size

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