3

import pygame as pg
def create_window(width, height):
    """create a width x height resizable window/frame"""
    win = pg.display.set_mode((width, height), pg.RESIZABLE)
    # optional fill bg red, default is black
    win.fill((0, 0, 0))
    # optional title info
    sf = "size x=%s  y=%s" % (width, height)
    pg.display.set_caption(sf)

    pg.display.flip()
    return win
pg.init()
width = 800
height = 500
win = create_window(width, height)
# event loop and exit conditions (windows titlebar x click)
while True:
    for event in pg.event.get():
        if event.type == pg.VIDEORESIZE:
            width, height = event.size
            # redraw win in new size
            win = create_window(width, height)
        if event.type == pg.QUIT:
            raise SystemExit