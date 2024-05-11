import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] ="hide" #to hide the ad message pygame prints.
import pygame
import generic_classes as gc
import shooting.cleaned_class as cc
import shooting.functions as func

def init(scr_rect:pygame.rect) -> dict:
    font=pygame.font.SysFont('Corbel',50)
    var={"quit":False,
         "menu":True,
         "rect":scr_rect,
         "clock":pygame.time.Clock(),
         "font":font,
         "menu_obj":{
             "help-txt":[font.render("This game is played with the mouse.",True,"black"),
                         font.render("What you need to do is to click",True,"black"),
                         font.render("On the UFOs that will appear while playing.",True,"black"),
                         font.render("At the start the UFOs will spawn slowly.",True,"black"),
                         font.render("They will later spawn faster every time you reach",True,"black"),
                         font.render("a multiple of five destroyed UFOs.",True,"black"),
                         font.render("Click anywhere on the screen to start.",True,"black"),
                         font.render("",True,"black"),
                         font.render("To exit you can use the escape key.",True,"black")]
            }
         }
    var.update({ #adding all the sprites which needs the constant in var.
        "BG":func.resize(gc.Background(os.path.join("shooting","data","greenfield.jpg")).BG,(var["rect"].right,var["rect"].bottom)),
        })
    return var





def game_shooting(Screen:gc.Screen,fps:int):
    var=init(Screen.get_rect())
    time=0
    while not var["quit"]: #Game Loop
        keys=pygame.key.get_pressed()
        time+=1/fps
        if var["menu"]: #the menu
            Screen.blit(var["BG"],[0,0])
            Screen.fill("grey", special_flags=pygame.BLEND_RGBA_MIN)#make the translucent overlay.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:#When the big Red X at the top right is clicked
                    var["quit"]=True
                    return True
                if event.type == pygame.VIDEORESIZE:
                    var["rect"]=Screen.get_rect()
                    var["BG"]=func.resize(var["BG"],(var["rect"].right,var["rect"].bottom))

            if keys[pygame.K_ESCAPE] and time>0.25:
                var["quit"]=True

            if pygame.mouse.get_pressed()[0] and pygame.mouse.get_focused() and time>0.5:
                #the time condition is so that two actions (clicking on the game and starting playing)
                #Do happen on the same click.
                var["menu"]=False
                time=0
                sprite=[]
                sp_cd=1
                destroyed=0
                missed=0
                sp_time=5
                nxt_milestone=5
                #initiate the launch. (reset the variables)
            for i in range(0,len(var["menu_obj"]["help-txt"])):
                blit_location=[100,20+i*60]
                Screen.blit(var["menu_obj"]["help-txt"][i],blit_location)
                
        else : #the game itself
            Screen.blit(var["BG"],[0,0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#When the big Red X at the top right is clicked
                    var["quit"]=True
                    return True
                if event.type == pygame.VIDEORESIZE:
                    var["rect"]=Screen.get_rect()
                    var["BG"]=func.resize(var["BG"],(var["rect"].right,var["rect"].bottom))
            if keys[pygame.K_ESCAPE] :
                var["menu"]=True
                time=0
                #Add text with best score?
            
            sp_cd+=1/fps
            time+=1/fps
            if sp_cd>=sp_time:#make new ufos spawn
                sprite.append(func.load(var["rect"]))
                sp_cd=0

            #make it harder as the game is played.
            if destroyed>nxt_milestone:
                sp_time-=1
                nxt_milestone*=5
                if sp_time==0: sp_time=0.5 #at 3125 destroyed UFOs
                if sp_time<0: sp_time=0.2 #at 15625 destroyed UFOs (last effective milestone.)


            for sp in sprite:
                if sp.check_click():
                    sprite.remove(sp)
                    destroyed+=1
                sp.move(fps,var["rect"])
                sp.draw(Screen)
                if sp.check(var["rect"]): 
                    sprite.remove(sp)
                    missed+=1

            score=var["font"].render(f"Kill count: {destroyed}/{destroyed+missed}",True,"black")
            Screen.blit(score,[var["rect"].right-400,50])

        var["clock"].tick(fps)
        pygame.display.update()
        #end of the loop
    return False



#for testing purporses, you can run just this file.
#Will be removed when integrated inside the menu as it won't work anymore.
if __name__ == '__main__':
    pygame.init() #loads all of the pygame submodules
    Screen=cc.Screen()
    game_shooting(Screen,60)
    pygame.quit()