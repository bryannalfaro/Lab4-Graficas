import pygame
import random

BLACK  = (  0,   25,   255)
WHITE = (255,255,255)
class Life(object):
    def __init__(self, screen):
        self.screen = screen
        self.banderaCross = True
        self.cycle = 0
        _,_,self.width,self.height = self.screen.get_rect()

    def clear(self):
        self.screen.fill(BLACK)

    def pixel(self, x, y,color = WHITE):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()

    def render(self):
        beacon = [[(15,10),(16,10),(15,9),(16,9),(17,8),(18,8),(17,7),(18,7)],[(15,10),(16,10),(15,9),(18,8),(17,7),(18,7)]]
        tube = [(40,60),(41,59),(39,59),(40,58)]
        cube = [[(10,10),(11,10),(12,10)],[(10,10),(10,11),(10,12)],[(10,12),(11,12),(12,12)],[(12,12),(12,11),(12,10)]]
        '''

    Cualquier célula viva que tenga menos de dos vecinos vivos, muere. (underpopulation)
    Una célula viva que tenga dos o tres vecinos vivos, sobrevive. (survival)
    Cualquier célula viva que tenga más de tres vecinos vivos, muere. (overpopulation)
    Cualquier célula muerta que tenga exactamente tres vecinos vivos, vive. (reproduction)

        '''

        contador = 0
        print(self.width, self.height)
        vecinos = 0
        for i in range (1,self.width-1):
            for j in range (1,self.height-1):
                prev = self.prev_turn.get_at((i, j))
                if prev == WHITE:
                    try:

                        if self.prev_turn.get_at((i+1, j)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j+1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j-1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j+1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j-1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j-1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j+1)) == WHITE:
                            vecinos += 1
                        if vecinos < 2:
                            self.pixel(i, j, BLACK)
                        elif vecinos == 2 or vecinos == 3:
                            self.pixel(i, j, WHITE)
                        elif vecinos > 3:
                            self.pixel(i, j, BLACK)
                        vecinos = 0

                    except:
                        vecinos=0
                        pass


                else:
                    try:
                        if self.prev_turn.get_at((i+1, j)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j+1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i, j-1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j+1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j-1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i+1, j-1)) == WHITE:
                            vecinos += 1
                        if self.prev_turn.get_at((i-1, j+1)) == WHITE:
                            vecinos += 1
                        if vecinos ==3:
                            self.pixel(i, j, WHITE)
                        vecinos=0
                    except:
                        vecinos=0
                        pass
                        contador += 1
                        print("Fuera",contador)





        #print(self.prev_turn.get_at((x, y)))





