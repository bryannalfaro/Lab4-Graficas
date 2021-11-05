from life_generator import *
import pygame
import random
from sys import exit

pygame.init()
width = 300
height = 300
screen = pygame.display.set_mode((width, height))
r = Life(screen)

for i in range(int(width/10)*int(width/40)):
  first = random.randint(10,width-10)
  second = random.randint(10,height-10)
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


myfont = pygame.font.SysFont('Comic Sans MS', 10)
myfont2 = pygame.font.SysFont('Comic Sans MS', 9)



generations = 0
while True:
  pygame.event.get()
  pygame.time.delay(200)
  r.copy()
  r.clear()
  r.render()
  text = 'Generacion: ' + str(generations)
  text2 = 'Hecho por: Bryann Alfaro'
  textsurface = myfont.render(text, False, (255, 255, 0))
  textsurface2 = myfont2.render(text2, False, (255, 255, 0))
  screen.blit(textsurface,(width/2-80,height-20))
  screen.blit(textsurface2,(width/2+10,height-20))
  generations += 1
  for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

  pygame.display.flip()