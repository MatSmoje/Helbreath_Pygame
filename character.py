import pygame
import json, os
import datetime

class Character():
    def __init__(self,user, character, str, vit, dex, int, mag, char):
        self.file_saved_date = '2022-03-05'

        self.character_name = character
        self.account_name = user
    
        self.character_profile = ''
        self.character_location = None
        self.character_loc_map = 'lost'
        self.character_loc_x = 150
        self.character_loc_y = 151
        self.character_HP = 1550
        self.character_MP = 1525
        self.character_SP = 1400
        self.character_LEVEL = 1
        self.character_RATING = 0
        self.character_STR = str
        self.character_INT = int
        self.character_VIT = vit
        self.character_DEX = dex
        self.character_MAG = mag
        self.character_CHARISMA = char
        self.character_LUCK = 1
        self.character_EXP = 1
        self.character_LU_Pool= 1
        self.admin_user_level = 0
        self.character_EK_Count = 0
        self.character_PK_Count= 0
        self.character_reward_gold= 0
        self.character_downskillindex= 0
        self.character_IDnum1= 26
        self.character_IDnum2= 6
        self.character_IDnum3= 1990
        self.sex_status= 1
        self.skin_status= 1
        self.hairstyle_status= 1
        self.haircolor_status= 1
        self.underwear_status= 1
        self.super_attack_left= 0

        self.data = {
                "FILE-DATE":
                {
                    "file-saved-date": self.file_saved_date
                },
                "NAME-ACCOUNT":
                {
                    "character-name": self.character_name,
                    "account-name": self.account_name
                },
                "STATUS":
                {
                    "character-profile": self.character_profile,
                    "character-location": self.character_location,
                    "character-loc-map": self.character_loc_map,
                    "character-loc-x": self.character_loc_x,
                    "character-loc-y": self.character_loc_y,
                    "character-HP": self.character_HP,
                    "character-MP": self.character_MP,
                    "character-SP": self.character_SP,
                    "character-LEVEL": self.character_LEVEL,
                    "character-RATING": self.character_RATING,
                    "character-STR": self.character_STR,
                    "character-INT": self.character_INT,
                    "character-VIT": self.character_VIT,
                    "character-DEX": self.character_DEX,
                    "character-MAG": self.character_MAG,
                    "character-CHARISMA": self.character_CHARISMA,
                    "character-LUCK": self.character_LUCK,
                    "character-EXP": self.character_EXP,
                    "character-LU_Pool": self.character_LU_Pool,
                    "admin-user-level": self.admin_user_level,
                    "character-EK-Count": self.character_EK_Count,
                    "character-PK-Count": self.character_PK_Count,
                    "character-reward-gold": self.character_reward_gold,
                    "character-downskillindex": self.character_downskillindex,
                    "character-IDnum1": self.character_IDnum1,
                    "character-IDnum2": self.character_IDnum2,
                    "character-IDnum3": self.character_IDnum3,
                    "sex-status": self.sex_status,
                    "skin-status": self.skin_status,
                    "hairstyle-status": self.hairstyle_status,
                    "haircolor-status": self.haircolor_status,
                    "underwear-status": self.underwear_status,
                    "super-attack-left": self.super_attack_left
                }
            }
        print(type(self.data))


    def createNewChar(self):
        filename = 'S_Data/S_' + self.account_name + '/C_' + self.character_name + '.json'
        print(filename)
        with open(filename, "w") as file:
            json.dump(self.data, file, indent=4,  separators=(',',': '))

    def deleteCharacter(self, character):
        accFilename = 'S_Data/S_' + self.account_name + '/A_' + self.account_name + '.json'
        
        with open(accFilename, 'r+') as f:
            data = json.load(accFilename)
            data.remove(character)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        try:
            os.remove('/C_' + character + '.json')
        except:
            pass