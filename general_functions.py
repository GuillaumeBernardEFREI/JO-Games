import generic_classes as gc
import pygame as pg
import os
import shooting.rvpd_shooting as shooting
import basketball.main as basketball
import Goodminton.Goodminton as Goodminton
from javlot.main import javlot

def init() -> dict:
    """
    Function to create the variables used in main.
    """
    var={}
    size=(960,540)
    sc=gc.Screen(size,"JO-Games")
    var["Win"]=sc.win
    var["Running"]=True
    var["clock"]=clock=pg.time.Clock()
    var["fps"]=30

    #initializing the size with calculations:
    var["Sizes"]={"max_x":10000,"max_y":10000,"game-x":2500,"game-y":3500,"sep-x":625,"sep-y":1000}

    var["Background"]=gc.Background(os.path.join("data","size.png")).BG
    var["Games"]={"game-1":gc.General_Game_Object(os.path.join("data","Badminton.jpg")),
                  "free-1":gc.General_Game_Object(None,transparent=True),
                  "game-2":gc.General_Game_Object(os.path.join("data","basket.png")),
                  "game-3":gc.General_Game_Object(os.path.join("data","shooting.jpg")),
                  "free-2":gc.General_Game_Object(None,transparent=True),
                  "game-4":gc.General_Game_Object(os.path.join("data","javelot.png"))}

    
    var["Win"],var["gamesep"],var["display_Games"],var["disp_Background"],var["gamepos"]=all_resize(size,var["Sizes"],var["Games"],var["Background"])
    #i am using display variables to not loose resolution by resizing multiple time the same image. 
    return var

def win_resize(size:pg.rect) -> pg.display:
    """
    Function which recreates the screen every time the window is resized.
    This is a seemless transition.
    """
    sc=gc.Screen(size,"JO-Games")
    return sc.win

def all_resize(size:tuple[int,int],Sizes:dict[int],games:dict[gc.General_Game_Object],BG:gc.Background) -> tuple:
    """
    Functions which recalls all the functions to get back the "hard-codded" coordonates of everything.
    No matter the size of the screen.
    
    This function is called every time the window is resized.
    """
    gamesep=resize_gamesep(Sizes,size)
    sc=win_resize(size)
    games=resize_game_obj(games,gamesep)
    BG=pg.transform.scale(BG,size)
    gamepos=gamespos(gamesep)
    return sc,gamesep,games,BG,gamepos

def resize_gamesep(Sizes:dict[int],winsize:pg.rect) -> dict[float]:
    """
    Function to create/remake the gamesep variable which chooses the distance
    between the different games.
    """
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

def resize_game_obj(games:dict[gc.General_Game_Object],gamesep:dict[float]) -> dict[gc.General_Game_Object]:
    """
    Function to resize all the given games
    """
    for game in games:
        games[game].resize((gamesep["game-x"],gamesep["game-y"]))
    return games

def display_games(win:pg.display,games:dict[str:gc.General_Game_Object],Sizes:dict[str:int]) -> None:
    """
    Function which displays (in the window) all the games inside 'games' variable.
    """
    posx=Sizes["sep-x"]
    posy=Sizes["sep-y"]
    for game in games:
        #games[game].get_rect().
        win.blit(games[game].sprite,[posx,posy])
        posx+=Sizes["game-x"]
        posx+=Sizes["sep-x"]
        if posy>=Sizes["max_y"]:
            raise NotImplementedError("there is not multiple pages of games right now")
            #if there are more than 6 game.
        if posx>=Sizes["max_x"]:
            posx=Sizes["sep-x"]
            posy+=Sizes["sep-y"]+Sizes["game-y"]

def gamespos(gamesep) -> list[tuple[float,float]]:
    """
    Function called to find the position at which every game should be blitted to.
    """
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

def checkcolision(mousepos:tuple[float,float],Games:dict[str:gc.General_Game_Object],gamepos:list[tuple[float,float]]) -> int:
    """
    Function to verify if the player clicks on a game.
    """
    i=0
    for game in Games:
        rect=Games[game].sprite.get_rect()
        rect.x=gamepos[i][0]
        rect.y=gamepos[i][1]
        if rect.collidepoint(mousepos):
            if game=="game-1":
                return 1
            if game=="game-2":
                return 2
            if game=="game-3":
                return 3
            if game=="game-4":
                return 4
        i+=1
    return 0 #did not click a game

def play_game(game:int,screen:pg.display,fps:int) -> bool:
    """
    Function to call the games clicked
    So that The check collision doesn't have too many variables.

    Returns a bool, false to say that you continue or True to say to close the screen.
    """
    if game==1:
        screen=win_resize((1450, 840))
        screen.fill("black")
        Goodminton.Goodminton(screen)
    elif game==2:
        screen=win_resize((950, 600))#hard coded in the game code.
        screen.fill("black")# to not have unwanted image continue beeing seen.
        basketball.basketball(screen)
    elif game==3:

        if (shooting.game_shooting(screen,fps)==True): #True means to totally quit the game.
            return True
    elif game==4:
        screen=win_resize((1080,720))
        screen.fill("black")
        javlot(screen)


    return False
