from math import *
import pygame
import os
import pygame.locals

class Vector2:
    def __eq__(self,u)->bool:
        return (self.x==u.x and self.y==u.y)
    def __repr__(self)->str:
        return "[ "+str(self.x)+" , "+str(self.y)+" ]"
    def __init__(self,x=0.0,y=0.0):
        self.x,self.y =x,y
    def __str__(self)->str:
        return "[ "+str(self.x)+" , "+str(self.y)+" ]"
    def __add__(self,u):
        # u must be a Vector2, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x+u.x,self.y+u.y)
        return Vector2(self.x+u,self.y+u)
    def __sub__(self,u):
        # u must be a Vector3, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x-u.x,self.y-u.y)
        return Vector2(self.x-u,self.y-u)
    def __truediv__(self,u):
        # u must be a Vector3, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x/u.x,self.y/u.y)
        return Vector2(self.x/u,self.y/u)
    def __mul__(self,u):
        # u must be a Vector3, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x*u.x,self.y*u.y)
        return Vector2(self.x*u,self.y*u)
    def frac(self):
        return Vector2(self.x%1,self.y%1)
    def rotate(self,rotation):
        #https://en.wikipedia.org/wiki/Rotation_matrix
        rotation *= (pi/180)

        return Vector2()
    def normalize(self):
        # normalize the vector (self**2 =1)
        d = sqrt(self.x**2+self.y**2)
        return Vector2(self.x/d,self.y/d)
    def _fabs(self):
        return Vector2(fabs(self.x),fabs(self.y))
    def dotProduct(self,u,isAbs=False)->float:
        #return the dot product of 2 vector2
        if not isAbs:
            return self.x*u.x+self.y*u.y
        return fabs(self.x*u.x)+fabs(self.y*u.y)
    def _sum(self)->float:
        # return the sum of x and y
        return self.x+self.y
    def distance(self,u,doSqrt)->float:
        # return the distance between two points
        # doSqrt=True -> use square root
        # else return square distance
        if doSqrt:
            return sqrt(((self-u)*(self-u))._sum())
        return ((self-u)*(self-u))._sum()


class Screen(pygame.Surface):
    def __init__(self):
        size=1450,840
        pygame.Surface.__init__(self,size)
        self.screen=pygame.display.set_mode(size)


class Background(pygame.sprite.Sprite):
    def __init__(self,path):
            pygame.sprite.Sprite.__init__(self)
            self.BD=pygame.image.load(path).convert()

class General_Game_Object(pygame.sprite.Sprite):
    def __init__(self,img_path, *args, **kargs):#*args and **kargs are if you don't want to have these values in all the classes but only in some that you created.
        pygame.sprite.Sprite.__init__(self)
        self.sprite=pygame.image.load(img_path).convert_alpha()#The convert alpha should make the transparent pixels in png really transparent in pygame.
        if "resize" in kargs:
            self.resize(kargs['resize'])

    def resize(self,values):
        self.sprite = pygame.transform.scale(self.sprite,values)

    def rect(self):
        return self.sprite.get_rect()
    #rect is the position of the sprite.