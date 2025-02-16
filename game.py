import pgzrun
import random
from time import time

WIDTH = (600)
HEIGHT = (400)

starttime = 0
totaltime = 0

nextsatelite = 0
lines = []

satelites = []
totalsatelites = (8)
def createsatelites():
    global starttime, totaltime
    for i in range(8):
        satelite = Actor("satelite.png")
        satelite.pos = random.randint(30, 570), random.randint(30, 370)
        satelites.append(satelite)
    starttime = time()


def draw():
    global starttime, totaltime
    global nextsatelite
    screen.blit("space.png", (0, 0))
    number = 1
    for i in satelites:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        i.draw()
        number += 1
    for i in lines:
        screen.draw.line(i[0], i[1], "white")
    if nextsatelite < totalsatelites:
        totaltime = time() - starttime
        screen.draw.text(str(round(totaltime, 1)), (10, 10), fontsize = 30, color = ("white"))
    else:
        screen.draw.text(str(round(totaltime, 1)), (10, 10), fontsize = 30, color = ("white"))
        screen.fill("red")
        screen.draw.text("game over", (175, 175), fontsize = 100, color = ("white"))
        screen.draw.text("total time taken :" + str(round(totaltime, 1)), (175, 300), fontsize = 50, color =  ("white"))


def on_mouse_down(pos):
    global lines, nextsatelite
    if nextsatelite < totalsatelites:
        if satelites[nextsatelite].collidepoint(pos):
            if nextsatelite:
                lines.append((satelites[nextsatelite-1].pos, satelites[nextsatelite].pos))
            nextsatelite += 1
        else:
            lines = []
            nextsatelite = 0

def update():
    pass

createsatelites()

pgzrun.go()