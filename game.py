import pygame
import time
from PIL import Image
from pygame.locals import *
import initGame, textInput, checkLogin



running = True

pygame.mixer.init()  # Initialize the mixer module.


def main():
    global running
    pygame.init()
    screen = pygame.display.set_mode((640, 480)) #screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
    pygame.display.set_caption("Helbreath Cabito")

    e14 = pygame.mixer.Sound('SOUNDS/E14.WAV') # Click Sound

    # Creación de objetos
    login = initGame.StartGame(screen)
    accountBox = textInput.inputText(180, 158, screen)
    passwdBox = textInput.inputText(180, 180, screen)
    checkCredent = checkLogin.BbddLogin()
    textBoxs = [accountBox,passwdBox]
    
    while running:
        ev = pygame.event.get()
        pos = pygame.mouse.get_pos()
        #print(pos)


        screen.fill((0,0,0))
        login.cursor()
        mouseHoverDetect = login.startGame() # Menu MouseHover

        #print(login.startGameVar)
        #print("State of mouseHover: " +str(mouseHoverDetect))
        
        if login.startGameVar == 2: 
            for box in textBoxs:
                box.draw()
        
        
        
        



        # time = pygame.time.get_ticks()
        
            
        
        for event in ev:

            if login.accountState:
                accountBox.write(event)
                    
            if login.passwordState:
                passwdBox.write(event,True)
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouseHoverDetect == 1:
                    e14.play()
                    print("Login Buttn pressed")
                    login.startGameVar = 1

                if mouseHoverDetect == 2:
                    e14.play()  
                    print("newAccount Buttn pressed") ####################################
                    login.startGameVar = 3
                
                if mouseHoverDetect == 3:
                    e14.play()  
                    print("Select Server: Cancel Buttn pressed")
                    login.startGameVar = 0
                
                if mouseHoverDetect == 4:
                    e14.play()  
                    print("Abaddon Serv")
                    login.accountState = True
                    login.startGameVar = 2
                
                if mouseHoverDetect == 5:
                    e14.play()  
                    print("Apocalypse Serv")
                    login.startGameVar = 2
                
                if mouseHoverDetect == 6:
                    e14.play()  
                    print("Write Credentials: Cancel Button Pressed")
                    login.startGameVar = 1
                    login.accountState = False
                    login.passwordState = False
                    accountBox.cleanLoginData()
                    passwdBox.cleanLoginData()
                    

                if mouseHoverDetect == 7:
                    e14.play()  
                    print("Connect")
                    user =  accountBox.getData()
                    passwd = passwdBox.getData()
                    if checkCredent.checkCredentials(user,passwd):
                        login.startGameVar = 3  # Estado Logeado
                    accountBox.cleanLoginData()
                    passwdBox.cleanLoginData()
                    
                if mouseHoverDetect == 8:
                    e14.play()
                    login.accountState = True
                    login.passwordState = not login.accountState
                    print("Write Credentials: Account Active")
                    
                    # Creamos objeto de escucha de texto
                    
                
                if mouseHoverDetect == 9:
                    e14.play()
                    login.passwordState = True
                    login.accountState = not login.passwordState
                    
                    print("Write Credentials: Passwd Active")
                    # Creamos objeto de escucha de texto
                    
                    # login.startGameVar = 0
                    
### Select character 10, 11, 12, 13, 14, 15, 16, 17, 18
                if mouseHoverDetect == 10:
                    e14.play()
                    login.charSelection = 0
                    print("Char List: 1")
                
                if mouseHoverDetect == 11:
                    e14.play()
                    login.charSelection = 1
                    print("Char List: 2")

                if mouseHoverDetect == 12:
                    e14.play()
                    login.charSelection = 2
                    print("Char List: 3")

                if mouseHoverDetect == 13:
                    e14.play()
                    login.charSelection = 3
                    print("Char List: 4")
                    
                if mouseHoverDetect == 14:
                    e14.play()
                    print("Char List: Start")
                    
                if mouseHoverDetect == 15:
                    e14.play()
                    print("Create Char")
                    login.startGameVar = 4
                    
                if mouseHoverDetect == 16:
                    e14.play()
                    print("")
                    
                if mouseHoverDetect == 17:
                    e14.play()
                    print("")
                    
                if mouseHoverDetect == 18: # Logout From Select Character
                    e14.play()
                    login.accountState = False
                    login.passwordState = False
                    
                    login.startGameVar = 0
                
                if mouseHoverDetect == 19: # Cancel create new Character
                    login.str = 10
                    login.vit = 10
                    login.dex = 10
                    login.int = 10
                    login.mag = 10
                    login.chr = 10 
                    login.specialStatPoints = 10 
                    login.startGameVar = 3
                    
                if mouseHoverDetect == 20:
                    login.startGameVar = 5
                
                if mouseHoverDetect == 21:
                    if login.specialStatPoints > 0 and login.str <= 13 and login.str >= 9:
                        login.str = login.str + 1
                        login.specialStatPoints = login.specialStatPoints - 1

                if mouseHoverDetect == 22:
                    if login.specialStatPoints <= 14 and login.str <= 14 and login.str >= 11:
                        login.str = login.str - 1
                        login.specialStatPoints = login.specialStatPoints + 1
                
                if mouseHoverDetect == 23:
                    if login.specialStatPoints > 0 and login.vit <= 13 and login.vit >= 9:
                        login.vit = login.vit + 1
                        login.specialStatPoints = login.specialStatPoints - 1
                    
                if mouseHoverDetect == 24:
                    if login.specialStatPoints <= 14 and login.vit <= 14 and login.vit >= 11:
                        login.vit = login.vit - 1
                        login.specialStatPoints = login.specialStatPoints + 1

                if mouseHoverDetect == 25:
                    if login.specialStatPoints > 0 and login.dex <= 13 and login.dex >= 9:
                        login.dex = login.dex + 1
                        login.specialStatPoints = login.specialStatPoints - 1
                    
                    
                if mouseHoverDetect == 26:
                    if login.specialStatPoints <= 14 and login.dex <= 14 and login.dex >= 11:
                        login.dex = login.dex - 1
                        login.specialStatPoints = login.specialStatPoints + 1


                if mouseHoverDetect == 27:
                    if login.specialStatPoints > 0 and login.int <= 13 and login.int >= 9:
                        login.int = login.int + 1
                        login.specialStatPoints = login.specialStatPoints - 1
                     
                if mouseHoverDetect == 28:
                    if login.specialStatPoints <= 14 and login.int <= 14 and login.int >= 11:
                        login.int = login.int - 1
                        login.specialStatPoints = login.specialStatPoints + 1

                # MAG
                if mouseHoverDetect == 29:
                    if login.specialStatPoints > 0 and login.mag <= 13 and login.mag >= 9:
                        login.mag = login.mag + 1
                        login.specialStatPoints = login.specialStatPoints - 1
                     
                if mouseHoverDetect == 30:
                    if login.specialStatPoints <= 14 and login.mag <= 14 and login.mag >= 11:
                        login.mag = login.mag - 1
                        login.specialStatPoints = login.specialStatPoints + 1
                #CHR
                if mouseHoverDetect == 31:
                    if login.specialStatPoints > 0 and login.chr <= 13 and login.chr >= 9:
                        login.chr = login.chr + 1
                        login.specialStatPoints = login.specialStatPoints - 1
                     
                if mouseHoverDetect == 32:
                    if login.specialStatPoints <= 14 and login.chr <= 14 and login.chr >= 11:
                        login.chr = login.chr - 1
                        login.specialStatPoints = login.specialStatPoints + 1

                if mouseHoverDetect == 33: # WARRIOR DEFAULT SET
                    login.str = 14
                    login.vit = 12
                    login.dex = 14
                    login.int = 10
                    login.mag = 10
                    login.chr = 10 
                    login.specialStatPoints = 0

                if mouseHoverDetect == 34: # MAGE DEFAULT SET
                    login.str = 10
                    login.vit = 12
                    login.dex = 10
                    login.int = 14
                    login.mag = 14
                    login.chr = 10 
                    login.specialStatPoints = 0

                if mouseHoverDetect == 35: # MASTER DEFAULT SET
                    login.str = 14
                    login.vit = 10
                    login.dex = 12
                    login.int = 10
                    login.mag = 10
                    login.chr = 14 
                    login.specialStatPoints = 0
                
                    





                
                if mouseHoverDetect == 99:
                    e14.play()
                    login.startGameVar = 99
                    


            if event.type == pygame.QUIT:
                login.startGameVar = 99
                
                
                
        if login.exitTrigger == True:
            running = False
                    
        
        pygame.display.update()


main()