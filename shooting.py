import pygame
import time,os
import pygame.locals

size = height,length = 420,420
pygame.init()
screen = pygame.display.set_mode(size, pygame.locals.RESIZABLE)
#for a file in "JO-GAMES/data/"
image=pygame.image.load(os.path.join("data","test.png"))
running=True
while running:
    size=screen.get_size()
    screen.blit(pygame.transform.scale(image,size),[0,0]) #draws the image at position 0,0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#When the big Red X at the top right is clicked
            running = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running=False #When the key Esc is clicked
pygame.quit()

import random

if __name__=='__main__': 
    # this code is to test only, it will run always when we manually run the code.
    pass