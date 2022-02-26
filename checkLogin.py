import pygame

class BbddLogin():
    def __init__(self):
        self.user = 'anton'
        self.passwd = 'xasdxasd'
    
    def checkCredentials(self, user, passwd):
        if self.user == user and self.passwd == passwd:
            return True
        else:
            return False
