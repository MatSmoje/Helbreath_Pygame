import os, struct, mmap
import io
from PIL import Image, ImageDraw
from collections import namedtuple
import pygame

exists = lambda fn: os.path.exists(fn) and os.path.isfile(fn)

DEF_PAKSIG = b"<Pak file header>"
DEF_SPRSIG = b"<Sprite File Header>"

class Frame:
    def __init__(self, *args):
        (self.X, self.Y, self.W,self.H, self.FX, self.FY) = args[0]


class Sprite:
    def __init__(self):
        self.frames = []
        self.image = None

    def add_frame(self, fr):
        self.frames += [Frame(fr)]
    
    def get_Frames(self):
        return self.frames



class HBPak(object):

    def __init__(self, filename):
        assert exists(filename)
        self.PakFileName = filename
     
    def prepareSprite(self, imagen):
        data = imagen.tobytes()
        mode = imagen.mode
        size = imagen.size
        image1 = pygame.image.fromstring(data, size, mode)
        return image1

    def load(self):
        f  = open(self.PakFileName, "r+b")
        fs = mmap.mmap(f.fileno(), 0)

        try:
            CheckChar = fs[:len(DEF_PAKSIG)]
            if CheckChar != DEF_PAKSIG:
                print(CheckChar)
                return False
            fs.seek(20)
            SprOffsets = []
            (c1, ) = struct.unpack('<I', fs.read(4)) #sprcount
            self.sprites = []
            self.frames = []

            for i in range(c1):
                (off, size) = struct.unpack('<II' , fs.read(8))
                SprOffsets  += [(off, size)]
            PakFileName = self.PakFileName.split('/')[1]
            spritesList = { }
            spritesList[PakFileName] = { }
            spritesList[PakFileName]['length'] = len(SprOffsets)
            spritesList[PakFileName]['sprites'] = {}
            spritesList[PakFileName]['frames'] = {}
            contSpr = 0
             

            for i in range(len(SprOffsets)):
                #print("Sprite count: " + str(i))
                (offset, size) = SprOffsets[i]
                fs.seek(offset, 0)
                head = fs.read(100)
                assert head[:len(DEF_SPRSIG)] == DEF_SPRSIG
                (c2, ) = struct.unpack('<I', fs.read(4))
                Spr = Sprite()
                frames = []
                for j in range(c2):
                    #print("Subframe: " + str(j))
                    #self.frames.append(struct.unpack('<6h', fs.read(12)))    # ESTE PARA FRAMES
                    frames += [(struct.unpack('<6h', fs.read(12)))]
                    #Spr.add_frame()
                fs.seek(4, os.SEEK_CUR)
                data = io.BytesIO(fs.read(size))
                Spr.image = Image.open(data).convert("RGBA")
                #self.sprites += [Spr.image]
                spritesList[PakFileName]['sprites'][contSpr] = self.prepareSprite(Spr.image)
                spritesList[PakFileName]['frames'][contSpr] = frames
                contSpr += 1
                
            
                
        finally:
            fs.close()
            f.close()

        #return 
        return spritesList






    

    
                                            
            
            
