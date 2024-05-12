import pygame
import os
import pygame.locals
from javlot.vector import Vector2
from random import randint
import pygame
import os
from math import sin,pi,acos
pygame.font.init()
class javelot(object):
    def __init__(self,position,velocity):
        """ The constructor of the class """
        self.velocity = velocity*3

        self.time=0

        self.fixed=False
        self.image = pygame.image.load(os.path.join("javlot",os.path.join("data","javelot.png")))
        self.a=self.image
        self.position=position
        self.initialePos=position
        self.acceleration=Vector2(0,9.81)
        #acceleration
        self.tick()

    def tick(self):
        if self.fixed:
            return
        self.time+=7.5/60
        self.nextPos=  self.acceleration * (self.time ** 2) + self.velocity * self.time+self.initialePos
        if (self.position-self.nextPos).y>0:
            self.r=-180/pi*acos((self.position-self.nextPos).normalize().dotProduct(Vector2(1,0)))
        else:
            self.r = 180 / pi * acos((self.position - self.nextPos).normalize().dotProduct(Vector2(1, 0)))

        self.position = self.nextPos
        global score
        global touchedBaloons

        score = int(self.position.x) * (touchedBaloons+1)
        if self.position.y>630 and not self.fixed:
            global  baloons
            baloons = []
            for i in range(5):
                baloons.append(baloon(Vector2(randint(150, 1000), randint(175, 500))))
            self.position.y=640
            self.fixed=True
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        self.a=pygame.transform.rotate(self.image,self.r)
        surface.blit(self.a, self.position.toTuple())
class baloon(object):
    def __init__(self, position):
        self.position = position
        self.p=position
        self.ispop=False
        self.time =randint(0,20)
    def tick(self):
        self.time+=1/10

        self.position=Vector2(self.p.x,int((self.p.y)+sin(self.time)*8))
        pygame.draw.circle(Window, (255, 50, 50, 100),self.position.toTuple() , 23)


class Screen(pygame.Surface):
    def __init__(self):
        size=1080,720
        pygame.Surface.__init__(self,size)
        self.screen=pygame.display.set_mode(size)
class Background(pygame.sprite.Sprite):
    def __init__(self,path):
        pygame.sprite.Sprite.__init__(self)
        self.BD=pygame.image.load(path).convert()

Window=None
clock=None
running=True
#mouse input information
mousePressed=False
mousePressedPos=Vector2()
mouseReleasedPos=Vector2()
baloons=[]
#javelot
jav=None
mouseDistance=0
touchedBaloons=0
font = pygame.font.SysFont("freesansbold.ttf",100,False,False)
score=0

def javlot(scr_rect:pygame.rect):
    global  Window
    global  jav
    global  running
    global  mousePressed
    global  clock
    global  mousePressedPos
    global  mouseReleasedPos
    global  mouseDistance
    global  touchedBaloons
    global  baloons
    global  font
    global  score
    Window=scr_rect
    BG=Background(os.path.join("javlot",os.path.join("data","background.png"))).BD

    clock=pygame.time.Clock()
    running=True

    #mouse input information
    mousePressed=False
    mousePressedPos=Vector2()
    mouseReleasedPos=Vector2()
    baloons=[]
    for i in range(5):
        baloons.append(baloon(Vector2(randint(150,1000),randint(175,500))))
    #javelot
    jav=None
    mouseDistance=0
    touchedBaloons=0
    font = pygame.font.SysFont("freesansbold.ttf",100,False,False)
    score=0
    while running:
        score_display = font.render(str(score), 1, (0, 0, 0))
        Window.blit(pygame.transform.scale(BG, Window.get_size()), [0, 0])
        Window.blit(score_display, (20, 20))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running=False #When the key Esc is clicked
            return True
        if (jav == None or jav.fixed):
            pygame.draw.circle(Window, (255, 255, 255), (100, 600), 10)
            if pygame.mouse.get_pressed()[0] and mousePressed==False:
                mousePressed=True
                mousePressedPos=Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

            if pygame.mouse.get_pressed()[0] ==False and mousePressed==True:
                mousePressed=False
                mouseReleasedPos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                d = (Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) - mousePressedPos)
                if d.distance(Vector2(), False) > 10:
                    score = 0
                    touchedBaloons = 0;
                    direction = d.normalize()
                    jav=javelot(Vector2(100,600),direction*(-1*min(d.distance(Vector2(),True),50)))




            if mousePressed:
                mouseDistance=(min(Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]).distance(mousePressedPos,True)*0.1,30))
                d =(Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])-mousePressedPos)
                if d.distance(Vector2(),False)>0.01:
                    direction= d.normalize()
                    endPos=(mousePressedPos+ direction*mouseDistance * 10.0).toTuple()
                    pygame.draw.line(Window,(255,255,255),(int(mousePressedPos.x),int(mousePressedPos.y)),(int(endPos[0]),int(endPos[1])),int(mouseDistance*0.1))
                pygame.draw.circle(Window,(255,255,255),mousePressedPos.toTuple(),mouseDistance)
            if mouseDistance>0:
                mouseDistance-=7
                pygame.draw.circle(Window, (255, 255, 255,100), mousePressedPos.toTuple(), mouseDistance)

        if jav!=None:
            jav.tick()
            for i in baloons:
                i.tick()
                for j in range(10):
                    #pygame.draw.circle(Window, (0, 0, 255), (jav.position.x+jav.a.get_width()*0.5,jav.position.y+jav.a.get_height()*0.5), 10)
                    if (Vector2(jav.position.x+jav.a.get_width()*0.5,jav.position.y+jav.a.get_height()*0.5)).distance(i.position,True)<=23:
                        i.ispop=True
                        break
            a=0
            for i in range(len(baloons)):
                if baloons[i-a].ispop:
                    baloons.remove(baloons[i-a])
                    a+=1
                    touchedBaloons += 1
            jav.draw(Window)
        clock.tick(60)
        pygame.display.update()
    pygame.quit()
    exit()
#javlot(Screen().screen)
