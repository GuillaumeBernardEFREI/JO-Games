from math import *
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
    def norm(self) -> float:
        # normalize the vector (self**2 =1)
        d = sqrt(self.x**2+self.y**2)
        return d
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
    
class Trajectory:
    def __init__(self,use_velocity_vector:bool,launchvelocity:float,angleoflaunch:float,aceleration:float=9.81,start_velocity:Vector2=Vector2(1,1),startpos:Vector2=Vector2(0,0)) -> None:
        if use_velocity_vector:
            self.launchvelo=start_velocity.norm() # pythagoras
            self.ax=0 #The acceleration will only be the downward gravity for the moment (simplicity to understand)
            self.bx=start_velocity.x

            self.ay=aceleration/2
            self.by=start_velocity.y
        else:
            self.launchvelo=launchvelocity
            #because we use an euclidian system, we can consider the values beeing one of a right triangle.
            self.ax=0
            self.bx=launchvelocity*sin(angleoflaunch) #values are in radians

            self.ay=aceleration/2
            self.by=launchvelocity*cos(angleoflaunch) #angleoflaunch is in radians!

        self.cx=startpos.x
        self.cy=startpos.y

        #This equation represents y(x) and time has been eliminated.
        #The simplification is easy since we have chosen to have ax=0
        self.a=self.ay/(self.bx**2)
        self.b=-(2*self.ay)/(self.bx**2)      +self.by/(self.bx) #see calculations done on a sheet
        self.c=(self.ay*(self.cx**2))/(self.bx**2)    -(self.by*self.cx)/(self.bx)      +self.cy

        self.equation=f"y(x)={self.a}x^2+{self.b}x+{self.c}" #the equation is of the form ax^2+bx+c
                                # And the equation of this particular trajectory is stored into this string variable.
                                #this equation is only to be displayed in dev menus not to be used.
        self.startpos=startpos

    #    x = horizontal motion
    #    y = vertical motion
    def position(self,time,fixed:bool=False,screen_size:tuple|None=None) -> tuple:
        x=self.ax*(time**2)+self.bx*time
        y=self.ay*(time**2)+self.by*time
        if fixed: #The equation will be fixed to be calculated in a 10k*10k radius (only positive)
                # And then we render it down to the size of the screen, done here.
            if screen_size==None:
                raise TypeError("You need to give the screen size to make the equation a fixed one.")
            x*=screen_size[2]/10000 #screen size is the rect of the screen.
            y*=screen_size[3]/10000
        
        x+=self.cx
        y+=self.cy
        return (x,y) #sadly, we cannot output a vector2 because it won't work with pygame.

    def trajectory(self,nbpoints:int,starttime=0,maxtime=60,fixed:bool=False,screen_size:tuple|None=None)-> list[Vector2]:
        #maxtime is in seconds
        values=list()
        for i in range(starttime,nbpoints+1): #from time=0 to time=maxtime 
            time=i*maxtime/nbpoints
            pos=self.position(time,fixed,screen_size)
            values.append(pos)
        return values
    
    def highestpoint(self):
        return - self.b/(2*self.a)

    def hitfloor(self,floorheight): #returns the time of the equation when the floor is hit.
        root1=(self.b+sqrt((self.b**2)-4*self.a*(self.c-floorheight)))/(2*self.a)
        root2=(self.b-sqrt((self.b**2)-4*self.a*(self.c-floorheight)))/(2*self.a)
        if root1>=0 and root2>=0: #returns the highest root because the other one should be before the movement started.
            if root1>=root2:
                time=root1
            else:
                time=root2
            #time=(root1,root2)
        elif root1>=0:
            time = root1
        elif root2>=0:
            time = root2
        else :
            raise ValueError("The object should've touched the floor somewhere but it doesn't")
        return time

    def collisions(self,objects:list,trajectory):
        hit_obj=None
        for (xPOS,yPOS) in trajectory:
            #position=(xPOS,yPOS)
            #compute if the position will intersect or be inside one of the objects
            for (rect,pos_x,pos_y) in objects:
                #obj=(rect,pos_x,pos_y)
                #obj is of the form ( <rect([0](left),[1](top),[2](width),[3](height))>, pos_x, pos_y )

                #if position in the bounding box of the object
                #   pos_x+rect[0] <= xPOS <= pos_x+rect[2]
                #for the time beeing we are not using the rect [0] and [1] for positionning objects, but we may later so i make the code able to handle it.
                #   pos_y+rect[1] <= yPOS <= pos_y+rect[3]
                if (pos_x+rect[0] <= xPOS <= pos_x+rect[2] and pos_y+rect[1] <= yPOS <= pos_y+rect[3]):
                    if hit_obj is None:
                        hit_obj=(rect,pos_x,pos_y)
        return hit_obj

    def bounce(self,floorheight,hstop,bouncefactor,fixed=False,screen_size=None):
        #Please be careful, this action is irreversible.
        #hstop should be either a very little height or the height of the sprite (there shouldn't be a lot of diference)
        time =self.hitfloor(floorheight)#time when the floor is hit in the current expression.
        (self.cx,self.cy)=self.position(time,fixed,screen_size)
       #see https://stackoverflow.com/questions/573084/how-to-calculate-bounce-angle
        #v final: Vf = Vi + a * t 
        vf_x=self.launchvelo+self.ax*time
        vf_y=self.launchvelo+self.ay*time
        #Calculating the landing angle:
        land_angle=tanh(vf_y/vf_x)
        #https://www.quora.com/In-projectile-motion-from-a-height-how-do-you-find-the-landing-angle
        
        print(
"""For the time being this equation is not true to physics as i do not know how it works in physics.

Please be careful of this information!
        This print is located in the Classes.Trajectory.bounce function.""")
        self.launchvelo*=bouncefactor #making the speed go down
        self.bx=self.launchvelo*sin(land_angle) #values are in radians
        self.by=self.launchvelo*cos(land_angle)

        #same equation as before -> maynbe make a function
        self.b=-(2*self.ay)/(self.bx**2)      +self.by/(self.bx) #see calculations done on a sheet
        self.c=(self.ay*(self.cx**2))/(self.bx**2)    -(self.by*self.cx)/(self.bx)      +self.cy

        #check if the ball did bounce
        if self.highestpoint()>hstop:
            return True
        else:
            return False
        #returns True if the ball did bounce
        #returns False if the ball did not bounce
        #if false, make the object roll on the floor until it is out of the screen



    #It may be needed to do other type of movement later, for different type of bounces and all see https://en.wikipedia.org/wiki/Reflection_%28mathematics%29#Reflection_across_a_line_in_the_plane
        