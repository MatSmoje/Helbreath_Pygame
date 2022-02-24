import pygame
import time
from PIL import Image
from pygame.locals import *
import initGame



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
    
    while running:
        ev = pygame.event.get()
        pos = pygame.mouse.get_pos()


        screen.fill((0,0,0))
        login.cursor()
        menuStateI = login.startGame()
        
        
        
        
        

        # time = pygame.time.get_ticks()
        
        
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menuStateI == 1:
                    e14.play()
                    login.startGameVar = 1
                    print("Click")

                if menuStateI == 2:
                    e14.play()  
                    print("newAccount")

                if menuStateI == 3:
                    e14.play()  
                    print("exit")
                    login.startGameVar = 99
                    running = False

            if event.type == pygame.QUIT:
                login.startGameVar = 99
                running = False
                
        
        pygame.display.update()


main()