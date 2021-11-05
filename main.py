from life_generator import *
import pygame
import random
from sys import exit

pygame.init()
width = 300
height = 300
screen = pygame.display.set_mode((width, height))
life = Game(screen)

for i in range(int(width/10)*int(width/40)):
  first = random.randint(10,width-10)
  second = random.randint(10,height-10)
  life.generatingObjects(first,second)


myfont = pygame.font.SysFont('Comic Sans MS', 10)
myfont2 = pygame.font.SysFont('Comic Sans MS', 9)

pygame.display.set_caption('GAME OF LIFE')
pygame.display.set_icon(pygame.image.load('icon.jpg'))

speed = 200
generations = 0
while True:
  pygame.event.get()
  pygame.time.delay(speed)
  life.copyBuffer()
  life.clear()
  life.render()
  text = 'Generacion: ' + str(generations)
  text2 = 'Hecho por: Bryann Alfaro'
  text3 = 'UP key to speed'
  text4 = 'DOWN key to slow'
  text5 = 'SPEED: ' + str(speed)
  textsurface = myfont.render(text, False, (255, 255, 0))
  textsurface2 = myfont2.render(text2, False, (255, 255, 0))
  textsurface3 = myfont2.render(text3, False, (255, 255, 0))
  textsurface4 = myfont2.render(text4, False, (255, 255, 0))
  textsurface5 = myfont2.render(text5, False, (255, 255, 0))
  screen.blit(textsurface,(width/2-80,height-20))
  screen.blit(textsurface2,(width/2+10,height-20))
  screen.blit(textsurface3,(width/2+80,height-10))
  screen.blit(textsurface4,(width/2-20,height-10))
  screen.blit(textsurface5,(width/2-90,height-10))

  generations += 1
  for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed += 10

                if event.key == pygame.K_DOWN:
                    speed -= 10


  pygame.display.flip()