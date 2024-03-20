import generic_classes as gc
import pygame as pg
import os
import game1 as g1

def init() -> dict:
    var={}
    size=(420,420)
    sc=gc.Screen(size,"JO-Games")
    var["Win"]=sc.win
    var["Running"]=True
    var["clock"]=clock=pg.time.Clock()
    var["fps"]=30

    #initializing the size with calculations:
    var["Sizes"]={"max_x":10000,"max_y":10000,"game-x":2500,"game-y":3500,"sep-x":625,"sep-y":1000}

    var["Background"]=gc.Background(os.path.join("data","size.png")).BG
    var["Games"]={"game-1":gc.General_Game_Object(os.path.join("data","basket.png")).sprite,
                  "game-2":gc.General_Game_Object(os.path.join("data","basket.png")).sprite,
                  "game-3":gc.General_Game_Object(os.path.join("data","basket.png")).sprite,
                  "game-4":gc.General_Game_Object(os.path.join("data","basket.png")).sprite,
                  "game-5":gc.General_Game_Object(os.path.join("data","basket.png")).sprite,
                  "game-6":gc.General_Game_Object(os.path.join("data","basket.png")).sprite}

    
    var["Win"],var["gamesep"],var["display_Games"],var["disp_Background"]=all_resize(size,var["Sizes"],var["Games"],var["Background"])
    #i am using display variables to not loose resolution by resizing multiple time the same image. 
    var["gamepos"]=gamespos(var["gamesep"])
    return var

def win_resize(size):
    sc=gc.Screen(size,"JO-Games")
    return sc.win

def all_resize(size,Sizes,games,BG):
    gamesep=resize_gamesep(Sizes,size)
    sc=win_resize(size)
    games=resize_game_obj(games,gamesep)
    BG=pg.transform.scale(BG,size)
    return sc,gamesep,games,BG

def resize_gamesep(Sizes,winsize):
    gamesep=dict()
    multiplier_x=winsize[0]/Sizes["max_x"]
    multiplier_y=winsize[1]/Sizes["max_y"]
    gamesep["max_x"]=Sizes["max_x"]*multiplier_x
    gamesep["game-x"]=Sizes["game-x"]*multiplier_x
    gamesep["sep-x"]=Sizes["sep-x"]*multiplier_x

    gamesep["max_y"]=Sizes["max_y"]*multiplier_y
    gamesep["game-y"]=Sizes["game-y"]*multiplier_y
    gamesep["sep-y"]=Sizes["sep-y"]*multiplier_y
    return gamesep

def resize_game_obj(games,gamesep):
    for game in games:
        games[game]=pg.transform.scale(games[game],(gamesep["game-x"],gamesep["game-y"]))
    return games

def display_size(win_size:pg.Rect,obj_size:pg.Rect): 
    #The calculations are done on a 10k by 10k board
    #and here we calculate the position in which the object should be drawn of the screen
    pos_x=obj_size.x*win_size.x/10000
    pos_y=obj_size.y*win_size.y/10000
    return (pos_x,pos_y)

def display_games(win,games:dict[str:gc.General_Game_Object],Sizes:dict[str:int]):
    posx=Sizes["sep-x"]
    posy=Sizes["sep-y"]
    for game in games:
        #games[game].get_rect().
        win.blit(games[game],[posx,posy])
        posx+=Sizes["game-x"]
        posx+=Sizes["sep-x"]
        if posy>=Sizes["max_y"]:
            raise NotImplementedError("there is not multiple pages of games right now")
            #if there are more than 6 game.
        if posx>=Sizes["max_x"]:
            posx=Sizes["sep-x"]
            posy+=Sizes["sep-y"]+Sizes["game-y"]

def gamespos(gamesep):
    L=[]
    posx=gamesep["sep-x"]
    posy=gamesep["sep-y"]
    page_filled=False
    while page_filled==False:
        L.append((posx,posy))
        posx+=gamesep["game-x"]
        posx+=gamesep["sep-x"]
        if posy>=gamesep["max_y"]:
            page_filled=True
        if posx>=gamesep["max_x"]:
            posx=gamesep["sep-x"]
            posy+=gamesep["sep-y"]+gamesep["game-y"]
    return L 

def checkcolision(mousepos,Games,gamepos):
    i=0
    for game in Games:
        rect=Games[game].get_rect()
        rect.x=gamepos[i][0]
        rect.y=gamepos[i][1]
        if rect.collidepoint(mousepos):
            if game=="game-1":
                print("g1")
            if game=="game-2":
                print("g2")
            if game=="game-3":
                print("g3")
            if game=="game-4":
                print("g4")
            if game=="game-5":
                print("g5")
            if game=="game-6":
                print("g6")
        i+=1
    return 0

