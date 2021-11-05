import pygame
import random

BACKGROUND  = (  0,   25,   255)
CPOINT = (255,255,255)

class Life(object):
    def __init__(self, screen):
        self.screen = screen
        self.banderaCross = True
        self.cycle = 0
        _,_,self.width,self.height = self.screen.get_rect()

    def clear(self):
        self.screen.fill(BACKGROUND)

    def pixel(self, x, y,color = CPOINT):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()

    def render(self):
        '''
    Condiciones:
    Cualquier célula viva que tenga menos de dos vecinos vivos, muere. (underpopulation)
    Una célula viva que tenga dos o tres vecinos vivos, sobrevive. (survival)
    Cualquier célula viva que tenga más de tres vecinos vivos, muere. (overpopulation)
    Cualquier célula muerta que tenga exactamente tres vecinos vivos, vive. (reproduction)

        '''
        contador = 0
        vecinos = 0
        for i in range (1,self.width-1):
            for j in range (1,self.height-1):
                prev = self.prev_turn.get_at((i, j))
                if prev == CPOINT:
                    try:

                        if self.prev_turn.get_at((i+1, j)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j+1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j-1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j+1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j-1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j-1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j+1)) == CPOINT:
                            vecinos += 1
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
                        if self.prev_turn.get_at((i+1, j)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j+1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j-1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j+1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j-1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j-1)) == CPOINT:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j+1)) == CPOINT:
                            vecinos += 1
                        if vecinos ==3:
                            self.pixel(i, j, CPOINT)
                        vecinos=0
                    except:
                        vecinos=0
                        pass
                        contador += 1
                        print("Fuera",contador)





