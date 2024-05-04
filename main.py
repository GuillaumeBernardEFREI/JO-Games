import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] ="hide" #to hide the ad message pygame prints.
import pygame as pg
import general_functions as gf

var = gf.init()
#var["Win"].update()
pg.init()

#main loop
while var["Running"]:
    for event in pg.event.get():
        if event.type == pg.VIDEORESIZE:
            var["Win"],var["gamesep"],var["display_Games"],var["disp_Background"],var["gamepos"]=gf.all_resize(event.size,var["Sizes"],var["Games"],var["Background"])
            # redraw win in new size
        if event.type == pg.QUIT:
            var["Running"]=False
        if event.type == pg.MOUSEBUTTONDOWN:
            gf.checkcolision(pg.mouse.get_pos(),var["display_Games"],var["gamepos"])

    var["Win"].blit(var["disp_Background"],[0,0])
    gf.display_games(var["Win"],var["display_Games"],var["gamesep"])

    var["clock"].tick(var["fps"])
    pg.display.update()
#End of the loop.


pg.quit()
