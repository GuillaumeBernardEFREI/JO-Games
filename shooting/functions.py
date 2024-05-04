import pygame
import shooting.cleaned_class as cc
import os

def resize(obj:pygame.sprite,size:pygame.rect) -> pygame.sprite:
    obj=pygame.transform.scale(obj,size)
    return obj

def load(scr_rect:pygame.rect) -> cc.UFO:
    ufo=cc.UFO(os.path.join("shooting","data","red_circle.png"))
    ufo.gen_traj(scr_rect)
    return ufo
