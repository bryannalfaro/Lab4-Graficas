import pygame
import random

BACKGROUND  = (  0,   25,   255)
CPOINT = (255,255,255)

class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.banderaCross = True
        self.cycle = 0
        _,_,self.width,self.height = self.screen.get_rect()

    def clear(self):
        self.screen.fill(BACKGROUND)

    def pixel(self, x, y,color = CPOINT):
        self.screen.set_at((x, y), color)

    def copyBuffer(self):
        self.past_config = self.screen.copy()

    def generatingObjects(self,first,second):
        self.pixel(second,first)
        self.pixel(second+1,first)
        self.pixel(second+2,first)

        self.pixel(first,second)
        self.pixel(first+1,second)
        self.pixel(first,second-1)
        self.pixel(first+2,second-2)
        self.pixel(first+3,second-2)
        self.pixel(first+2,second-3)
        self.pixel(first+3,second-3)

        self.pixel(first,second)
        self.pixel(first,second-1)
        self.pixel(first,second-2)
        self.pixel(first-1,second-2)
        self.pixel(first-2,second-1)

    def render(self):
        '''
    Condiciones:
    Cualquier célula viva que tenga menos de dos vecinos vivos, muere. (underpopulation)
    Una célula viva que tenga dos o tres vecinos vivos, sobrevive. (survival)
    Cualquier célula viva que tenga más de tres vecinos vivos, muere. (overpopulation)
    Cualquier célula muerta que tenga exactamente tres vecinos vivos, vive. (reproduction)

        '''
        vecinos = 0
        for i in range (self.width):
            for j in range (self.height):
                prev = self.past_config.get_at((i, j))
                if prev == CPOINT:
                    try:

                        try:
                            if self.past_config.get_at((i+1, j)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i-1, j)) == CPOINT:
                                vecinos += 1
                        except:
                            pass

                        try:
                            if self.past_config.get_at((i, j+1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i, j-1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i+1, j+1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i-1, j-1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i+1, j-1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i-1, j+1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        if vecinos < 2:
                            self.pixel(i, j, BACKGROUND)
                        elif vecinos == 2 or vecinos == 3:
                            self.pixel(i, j, CPOINT)
                        elif vecinos > 3:
                            self.pixel(i, j, BACKGROUND)
                        vecinos = 0

                    except:
                        vecinos=0
                        pass


                else:
                    try:
                        try:
                            if self.past_config.get_at((i+1, j)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i-1, j)) == CPOINT:
                                vecinos += 1
                        except:
                            pass

                        try:
                            if self.past_config.get_at((i, j+1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i, j-1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i+1, j+1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i-1, j-1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i+1, j-1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        try:
                            if self.past_config.get_at((i-1, j+1)) == CPOINT:
                                vecinos += 1
                        except:
                            pass
                        if vecinos ==3:
                            self.pixel(i, j, CPOINT)
                        vecinos=0
                    except:
                        vecinos=0
                        pass





