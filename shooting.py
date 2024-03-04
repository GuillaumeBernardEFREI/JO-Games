#This file is currently a code dump to show how to make use of the other classes that have been coded.

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] ="hide" #to hide the ad message pygame prints.
import pygame
import pygame.locals
import classes
import cleaned_class as cc

pygame.init()
running=True

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
traj=classes.Trajectory(False,250.,1.57+1.,startpos=classes.Vector2(0,100))
#At multiples of pi, the trajectory will be vertical
#Between 0 and pi (non included) the trajectory will go the the right
#Over pi the trajectory will go to the left
#Between 0 and pi/2 the trajectory will only fall down
#Between pi/2 and pi (non included) the trajectory will create a parabola

#I recommend using high numbers for the launchvelocity to be able to have the parabola effect done.
points=traj.trajectory(100,fixed=True,starttime=-30,screen_size=Window.get_rect())
#pygame.draw.aalines(Window,"black",False,points)

ball=False
roll=False
#There is now a need to use a variable for the fps:
fps=20
#because it is too slow with only the time:
timefactor=20
floorheight=Window.get_rect().bottom-10
lowestheight=floorheight*0,8 #to change diminically later #or maybe just do a certain number +
bounceval=True

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
    eqtxt=font.render(traj.equation, True, "black")
    Window.blit(eqtxt,(10,20))

    #new code for the trajectory: (just redraw)
    #points=traj.trajectory(10)
    pygame.draw.aalines(Window,"black",False,points)
    #this instruction is to draw the trajectory but you can also move your object through this trajectory
    #by blitting the object to the values returned by Trajectory.position(time)

    #Now the code to make the object move.
    #Starts when pressing "k" on the keyboard
    if keys[pygame.K_k]:
        ball=True
        time=0
        traj=classes.Trajectory(False,150.,1.57+1.,startpos=classes.Vector2(0,100))
        maxheight=traj.highestpoint()
        floorheight=Window.get_rect().bottom-100 #in case the window has been resized
        lowestheight=Window.get_rect().bottom*0.8
        cd=0
        print(traj.highestpoint(),"\n",traj.equation)
        bounce=bounceval
        lowestheight=40

    if ball:
        objpos=traj.position(time,True,Window.get_rect())
        if cd>0: cd-=1/fps
        time+=(1/fps)*timefactor
        #objpos[0] = x, objpos[1] = y
        #print(objpos)
        if objpos[1] > floorheight:
            #print("passed 1")
            #objpos[1]+=Window.get_rect().bottom/10
            if cd<=0:
                if bounce:
                    bounce= traj.bounce(floorheight,lowestheight,time,0.9,True,Window.get_rect())
                    points=traj.trajectory(100,fixed=True,screen_size=Window.get_rect())
                    maxheight=traj.highestpoint()
                    cd=4/fps
                if not bounce:
                    ball=False
                    roll=True
                    (xpos,ypos)=objpos
                    print("Now rolling")
                time=0
        Window.blit(Bat,objpos)

        if objpos[0]>Window.get_rect().right or objpos[1]>Window.get_rect().bottom:#should be outside
            ball=False
            print("disappearing")


    if roll:
        xpos+=2.5
        Window.blit(Bat,(xpos,ypos))
        if xpos>Window.get_rect().right:
            roll=False
            print("finally erased")


    clock.tick(fps)#It is needed so that you don't go and have repeated the action a 100 times of going right in just one push.
    pygame.display.update()

pygame.quit()

if __name__=='__main__': 
    # this code is to test only, it will run always when we manually run the code.
    pass