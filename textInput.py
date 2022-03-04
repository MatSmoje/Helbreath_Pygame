import pygame 
import time



class inputText():
    def __init__(self, x, y, screen, text = ''):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 13)
        #self.font = pygame.font.Font('HB/FONTS/HAN3.FNT',13)
        self.activeColor = (255,255,255)
        self.timer = pygame.time.get_ticks()
        self.pos = pygame.mouse.get_pos()
        self.text = text
        self.passwd = text
        self.isPasswd = False
        self.txt_surface = self.font.render(text, True, self.activeColor)
        self.txt_surfaceBg = self.font.render(text, True, self.activeColor)
        self.x = x
        self.y = y


    
    def write(self, event, isPasswd = False):
        self.isPasswd = isPasswd
        self.active = True
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return True

                    #self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.passwd = self.passwd[:-1]
                else:
                    self.text += event.unicode
                    self.passwd += '*'
                # Re-render the text.
        return False
    
    def cleanLoginData(self):
        self.text = ''
        self.passwd = ''

    def render(self):
        if self.isPasswd:
            self.txt_surface = self.font.render(self.passwd, True, self.activeColor)
            self.txt_surfaceBg = self.font.render(self.passwd, True, (0,0,0))    
        else:
            self.txt_surface = self.font.render(self.text, True, self.activeColor)
            self.txt_surfaceBg = self.font.render(self.text, True, (0,0,0))
    

    
    def draw(self):
        self.render()
        self.cursor = pygame.Rect((self.x,self.y,7, 1))
        self.screen.blit(self.txt_surfaceBg, (self.x+1, self.y+1))
        self.screen.blit(self.txt_surface, (self.x, self.y))
        ## BLINK CURSOR
        if time.time() % 1 > 0.5:

            # bounding rectangle of the text
            text_rect = self.txt_surface.get_rect(topleft = (self.x,self.y+8))

            # set cursor position
            self.cursor.midleft = text_rect.midright

            pygame.draw.rect(self.screen, (0,0,0), self.cursor)
            pygame.draw.rect(self.screen, (255,255,255), self.cursor)


    def getData(self):
        auxiliar = self.text
        self.cleanLoginData()
        self.render()
        return auxiliar

    def writeText(self, mesage, x, y):
        color = (0,0,0)
        self.txt_surface = self.font.render(mesage, True, color)
        self.screen.blit(self.txt_surface, (x, y))
