import math

from pico2d import *

open_canvas()

grass = load_image('grass_png')

import os
os.getcwd()
'C:\\Python'
os.chdir('c:/MyRepo/2017184040_2DGP_DRILL/Homework06')
os.getcwd()
'c:\\MyRepo\\2017184040_2DGP_DRILL\\Homework06'
grass = load_image('grass_png')

os.listdir()

grass = load_image('grass_png')
character = load_image('character.png')

while True:
    run_circle()
    run_rectangle()
    break

def run_circle():
    print("CIRCLE")
    
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(deg/360 * 2 * math.pi)
        y = cy + r * math.sin(deg/360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.1)

def render_all(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def run_rectangle():
    print("RECTANGKE")
    # Bottom line
    for x in range(50, 750+1, 10):
        render_all(x, 90)
    # right line
    for y in range (90, 550+1, 10):
        render_all(750, y)
    #top line
    for x in range(750, 50-1, -10):
        render_all(x, 550)
    #left line
    for y in range(550, 90-1, -10):
        render_all(50, y)
    pass




