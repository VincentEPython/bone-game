import pgzrun
import random

WIDTH = 500
HEIGHT = 300

message = ""

# creating game character/actor
bone = Actor("bone")
bone.pos = (250,150)

def on_mouse_down(pos):
    global message
    if bone.collidepoint(pos):
        message = "Oh no you caught me"
        auto_pos()
    else:
      message = "catch me if you can"
def auto_pos():
    bone.x = random.randint(50,450)
    bone.y = random.randint(50,250)

def draw():
    screen.fill("grey")
    bone.draw()
    screen.draw.text(message,(0,0),color = "brown" , fontsize = 20 )

pgzrun.go()