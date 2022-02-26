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
    #screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Helbreath Cabito")

    e14 = pygame.mixer.Sound('SOUNDS/E14.WAV') # Click Sound

    # Creación de objetos
    login = initGame.StartGame(screen)
    
    accountBox = textInput.inputText( 180, 158, screen)
    passwdBox = textInput.inputText( 180, 180, screen)
    checkCredent = checkLogin.BbddLogin()
    textBoxs = [accountBox,passwdBox]
    
    while running:
        ev = pygame.event.get()
        pos = pygame.mouse.get_pos()
        #print(pos)


        screen.fill((0,0,0))
        login.cursor()
        menuStateI = login.startGame()
        
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
                if menuStateI == 1:
                    e14.play()
                    print("Login Buttn pressed")
                    login.startGameVar = 1

                if menuStateI == 2:
                    e14.play()  
                    print("newAccount Buttn pressed")
                
                if menuStateI == 3:
                    e14.play()  
                    print("Select Server: Cancel Buttn pressed")
                    login.startGameVar = 0
                
                if menuStateI == 4:
                    e14.play()  
                    print("Abaddon Serv")
                    login.accountState = True
                    login.startGameVar = 2
                
                if menuStateI == 5:
                    e14.play()  
                    print("Apocalypse Serv")
                    login.startGameVar = 2
                
                if menuStateI == 6:
                    e14.play()  
                    print("Write Credentials: Cancel Button Pressed")
                    login.startGameVar = 1
                    login.accountState = False
                    login.passwordState = False
                    

                if menuStateI == 7:
                    e14.play()  
                    print("Connect")
                    user =  accountBox.getData()
                    passwd = passwdBox.getData()
                    if checkCredent.checkCredentials(user,passwd):
                        login.startGameVar = 3  # Estado Logeado
                    
                if menuStateI == 8:
                    e14.play()
                    login.accountState = True
                    login.passwordState = not login.accountState
                    print("Write Credentials: Account Active")
                    
                    # Creamos objeto de escucha de texto
                    
                
                if menuStateI == 9:
                    e14.play()
                    login.passwordState = True
                    login.accountState = not login.passwordState
                    
                    print("Write Credentials: Passwd Active")
                    # Creamos objeto de escucha de texto
                    
                    # login.startGameVar = 0
                if menuStateI == 10:
                    e14.play()

                
                if menuStateI == 11:
                    e14.play()
                    print("")

                if menuStateI == 12:
                    e14.play()
                    print("")

                if menuStateI == 13:
                    e14.play()
                    print("")
                    
                if menuStateI == 14:
                    e14.play()
                    print("")
                    
                if menuStateI == 15:
                    e14.play()
                    print("")
                    
                if menuStateI == 16:
                    e14.play()
                    print("")
                    
                if menuStateI == 17:
                    e14.play()
                    print("")
                    
                if menuStateI == 18:
                    e14.play()
                    print("")
                    login.startGameVar = 0
                    
                
                
                
                if menuStateI == 99:
                    e14.play()
                    login.startGameVar = 99
                    running = False
                
                


            if event.type == pygame.QUIT:
                login.startGameVar = 99
                running = False
                
        
        pygame.display.update()


main()