import pygame 



class inputText():
    def __init__(self, x, y, screen, text = ''):
        self.screen = screen
        self.font = pygame.font.SysFont("Comic Sans", 13)
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
                    pass

                    #self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    self.passwd += '*'
                # Re-render the text.

    def render(self):
        if self.isPasswd:
            self.txt_surface = self.font.render(self.passwd, True, self.activeColor)
            self.txt_surfaceBg = self.font.render(self.passwd, True, (0,0,0))    
        else:
            self.txt_surface = self.font.render(self.text, True, self.activeColor)
            self.txt_surfaceBg = self.font.render(self.text, True, (0,0,0))
    

    
    def draw(self):
        self.render()
        self.screen.blit(self.txt_surfaceBg, (self.x+1, self.y+1))
        self.screen.blit(self.txt_surface, (self.x, self.y))

    def getData(self):
        auxiliar = self.text
        self.text = ''
        self.passwd = ''
        self.render()
        return auxiliar

    def writeText(self, mesage, x, y):
        color = (0,0,0)
        self.txt_surface = self.font.render(mesage, True, color)
        self.screen.blit(self.txt_surface, (x, y))
