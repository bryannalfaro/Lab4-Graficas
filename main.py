from life_generator import *
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((200, 200))
r = Life(screen)

[(15,10),
(16,10),
(15,9),
(16,9),
(17,8),
(18,8),
(17,7),
(18,7)]

for i in range(40):
  first = random.randint(10,180)
  second = random.randint(10,180)
  r.pixel(second,first)
  r.pixel(second+1,first)
  r.pixel(second+2,first)

  r.pixel(first,second)
  r.pixel(first+1,second)
  r.pixel(first,second-1)
  r.pixel(first+2,second-2)
  r.pixel(first+3,second-2)
  r.pixel(first+2,second-3)
  r.pixel(first+3,second-3)

  r.pixel(first,second)
  r.pixel(first,second-1)
  r.pixel(first,second-2)
  r.pixel(first-1,second-2)
  r.pixel(first-2,second-1)

'''r.pixel(44,40)
r.pixel(45,40)
r.pixel(46,40)

r.pixel(40,41)
r.pixel(41,41)
r.pixel(42,41)'''

myfont = pygame.font.SysFont('Comic Sans MS', 10)

generations = 0
while True:
  pygame.time.delay(300)
  r.copy()
  r.clear()
  r.render()
  text = 'Generacion: ' + str(generations)
  textsurface = myfont.render(text, False, (255, 255, 0))
  screen.blit(textsurface,(0,0))
  generations += 1

  pygame.display.flip()