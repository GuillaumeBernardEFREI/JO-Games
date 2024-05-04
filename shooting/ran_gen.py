import random as rd

def gen_eq(scr_size) -> list:
    case=rd.randint(1,4)

    if case==1: #from left
        maxy=scr_size.bottom
        velo=rd.randrange(1000,5000)
        anglelaunch=rd.random()*3.14
        x=-100
        y=rd.random()*maxy
        if y<maxy*0.1:
            y+=maxy*0.1
        if y>maxy*0.9:
            y-=maxy*0.1
        if anglelaunch<1.57:
            accmul=1
        else :
            accmul=-1
        if anglelaunch<0.5:
            anglelaunch+=0.5
        if anglelaunch>2.8:
            anglelaunch-=0.5

    elif case==2:#from top
        maxx=scr_size.right
        velo=rd.randrange(1000,5000)
        anglelaunch=rd.random()*3.14 -1.57 #from -1.57 to 1.57
        y=-100
        x=rd.random()*maxx
        if x<maxx*0.1:
            x+=maxx*0.1
        if x>maxx*0.9:
            x-=maxx*0.1
        accmul=10
        if anglelaunch<-1.3:
            anglelaunch+=0.3
        if anglelaunch>1.3:
            anglelaunch-=0.3

    elif case==3:#from right
        maxy=scr_size.bottom
        velo=rd.randrange(-5000,1000)
        anglelaunch=rd.random()*3.14
        x=scr_size.right
        y=rd.random()*maxy
        if y<maxy*0.1:
            y+=maxy*0.1
        if y>maxy*0.9:
            y-=maxy*0.1
        if anglelaunch<1.57:
            accmul=1
        else :
            accmul=-1
        if anglelaunch<0.5:
            anglelaunch+=0.5
        if anglelaunch>2.8:
            anglelaunch-=0.5

    else:#from bottom
        maxx=scr_size.right
        velo=rd.randrange(-5000,-1000)
        anglelaunch=rd.random()*3.14 -1.57 #from -1.57 to 1.57
        y=scr_size.bottom
        x=rd.random()*maxx
        if x<maxx*0.1:
            x+=maxx*0.1
        if x>maxx*0.9:
            x-=maxx*0.1
        accmul=-1000
        if anglelaunch<-1.3:
            anglelaunch+=0.3
        if anglelaunch>1.3:
            anglelaunch-=0.3
    
    startpos=(x,y)
    return [velo,anglelaunch,accmul,startpos]
