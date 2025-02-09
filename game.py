import pgzrun
import random
WIDTH = (600)
HEIGHT = (400)

nextsatelite = 0
lines = []

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


satelites = []
totalsatelites = (8)
def createsatelites():
    for i in range(8):
        satelite = Actor("satelite.png")
        satelite.pos = random.randint(30, 570), random.randint(30, 370)
        satelites.append(satelite)

def draw():
    global nextsatelite
    screen.blit("space.png", (0, 0))
    number = 1
    for i in satelites:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        i.draw()
        number += 1
    for i in lines:
        screen.draw.line(i[0], i[1], "white")

def update():
    pass

createsatelites()

pgzrun.go()