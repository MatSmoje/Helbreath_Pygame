import pygame
import testHbPak
from PIL import Image
from pygame.locals import *
import time
import json

class StartGame():
    def __init__(self, screen):
        self.screen = screen
        self.totalSprites = { }
        self.MakeSprite("New-Dialog.pak")
        self.MakeSprite("interface.pak")
        self.m_cLoading = 4
        self.startGameVar = 0 
        

    def printSprites(self, totalSprites):
        print(json.dumps(totalSprites, sort_keys=True, indent=2, default=str))

    
    def startGame(self):
        
        loading = self.totalSprites["New-Dialog.pak"]["sprites"][0]
        newAcc = self.totalSprites["New-Dialog.pak"]["sprites"][1]
        exit = self.totalSprites["New-Dialog.pak"]["sprites"][2]
        
        if self.m_cLoading == 100:
            logIn = self.totalSprites["LoginDialog.pak"]["sprites"][0]
        
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

        if self.startGameVar == 1:                              # Login
            data, mode, size = self.prepareSprite(logIn)
            image1 = pygame.image.fromstring(data, size, mode)
            rect = image1.get_rect()
            self.screen.blit(image1, rect)


            
            self.screen.blit(image1, (40,120), self.totalSprites["LoginDialog.pak"]["frames"][0][1][0:4])
            
            if pygame.Rect((260, 280), self.totalSprites["LoginDialog.pak"]["frames"][0][4][2:4]).collidepoint(pygame.mouse.get_pos()):
            # Cancel
                self.screen.blit(image1, (256,282), self.totalSprites["LoginDialog.pak"]["frames"][0][4][0:4])
                return 3
            # Abadon Server
            if pygame.Rect((139, 175), self.totalSprites["LoginDialog.pak"]["frames"][0][5][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(image1, (139,175), self.totalSprites["LoginDialog.pak"]["frames"][0][5][0:4])
                return 4
            # Apocalipsis Server
            if pygame.Rect((133, 205), self.totalSprites["LoginDialog.pak"]["frames"][0][6][2:4]).collidepoint(pygame.mouse.get_pos()):
                self.screen.blit(image1, (133,205), self.totalSprites["LoginDialog.pak"]["frames"][0][6][0:4])
                return 5
            
            #self.screen.blit(image1, self.totalSprites["LoginDialog.pak"]["frames"][0][0])
             

        if self.startGameVar == 99:                             # Exit
            data, mode, size = self.prepareSprite(exit)
            image1 = pygame.image.fromstring(data, size, mode)
            rect = image1.get_rect()
            self.screen.blit(image1, rect)
    
        
    
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



    #     pak = testHbPak.HBPak("Sprites/New-Dialog.pak")
    #     cursor = testHbPak.HBPak("Sprites/interface.pak")
        
    #     pass
        
