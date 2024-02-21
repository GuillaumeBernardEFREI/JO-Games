import pygame
import os
import pygame.locals
import classes

pygame.init()
running=True

class Screen(pygame.Surface):
    def __init__(self):
        size=420,420
        pygame.Surface.__init__(self,size)
        self.screen=pygame.display.set_mode(size,pygame.locals.RESIZABLE)


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

def draw_parabola(surface,points:dict):
    pygame.draw.aalines(surface,"black",False,points.values())

#Surface=Screen()
#Window= Surface.screen
Window=Screen().screen
#Background_sprite=Background(os.path.join("data","test.png"))
BG=Background(os.path.join("data","test.png")).BD

#Example for creating a General Game object:
Bat=General_Game_Object(os.path.join("data","bat.jpg"),resize=[100,100],alpha=True).sprite

pos_x=0
pos_y=0
clock=pygame.time.Clock()

#to render text:
font=pygame.font.SysFont(None,20)
#new code for the trajectory:
traj=classes.Trajectory(False,250.,1.57+1.,startpos=classes.Vector2(100,100))
#At multiples of pi, the trajectory will be vertical
#Between 0 and pi (non included) the trajectory will go the the right
#Over pi the trajectory will go to the left
#Between 0 and pi/2 the trajectory will only fall down
#Between pi/2 and pi (non included) the trajectory will create a parabola

#I recommend using high numbers for the launchvelocity to be able to have the parabola effect done.
points=traj.trajectory(100,fixed=True,starttime=-30,screen_size=Window.get_rect())
pygame.draw.aalines(Window,"black",False,points)

while running:
    #size=Screen.get_size()
    Window.blit(pygame.transform.scale(BG,Window.get_size()),[0,0]) #draws the image at position 0,0
    #Window.blit(Bat,[11,11])#Test value to know how it moves, (0,0) is the top left.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#When the big Red X at the top right is clicked
            running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False #When the key Esc is clicked
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        pos_x-=10
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        pos_y-=10
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        pos_x+=10
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        pos_y+=10
    if pos_x<0:
        pos_x=0
    if pos_x>Window.get_rect().bottom-100: #minus the size we resized the bat to
        pos_x=Window.get_rect().bottom-100  #minus the size we resized the bat to
    if pos_y<0:
        pos_y=0
    if pos_y>Window.get_rect().right-100:  #minus the size we resized the bat to
        pos_y=Window.get_rect().right-100  #minus the size we resized the bat to
    Window.blit(Bat,[pos_y,pos_x])
    #print(f"[{pos_x:2f},{pos_y:2f}]")

    #to write on the screen:
    postxt=font.render(f"[{pos_x:2f},{pos_y:2f}]", True, "black")
    Window.blit(postxt,(10,5))
    
    #new code for the trajectory: (just redraw)
    #points=traj.trajectory(10)
    pygame.draw.aalines(Window,"black",False,points)
    #this instruction is to draw the trajectory but you can also move your object through this trajectory
    #by blitting the object to the values returned by Trajectory.position(time)

    clock.tick(20)#It is needed so that you don't go and have repeated the action a 100 times of going right in just one push.
    pygame.display.update()

pygame.quit()

if __name__=='__main__': 
    # this code is to test only, it will run always when we manually run the code.
    pass