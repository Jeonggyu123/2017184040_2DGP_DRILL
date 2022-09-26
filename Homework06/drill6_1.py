Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math

from pico2d import *
Pico2d is prepared.

open_canvas()

grass = load_image('grass_png')
cannot load grass_png
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    grass = load_image('grass_png')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 349, in load_image
    raise IOError
OSError
import os
os.getcwd()
'C:\\Python'
os.chdir('c:/MyRepo/2017184040_2DGP_DRILL/Homework06')
os.getcwd()
'c:\\MyRepo\\2017184040_2DGP_DRILL\\Homework06'
grass = load_image('grass_png')
cannot load grass_png
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    grass = load_image('grass_png')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 349, in load_image
    raise IOError
OSError
os.listdir()
['.gitattributes', '.gitignore', 'character.png', 'character_grass.py', 'drill6.py', 'grass.png', 'pico.py']
img = pico2d.load_image
img = pico2d.load_image('character.png')


grass = load_image('grass_png')
cannot load grass_png
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    grass = load_image('grass_png')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 349, in load_image
    raise IOError
OSError
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print("CIRCLE")
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    delay(1)

    
def run_rectangle():
    print("RECTANGKE")
    pass

while True:
    run_circle()
    run_rectangle()
    break

CIRCLE
RECTANGKE
def run_circle():
    print("CIRCLE")
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    delay(1)

    
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


while True:
    run_circle()
    # run_rectangle()
    
    break

CIRCLE
CIRCLE
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    CIRCLE
NameError: name 'CIRCLE' is not defined
while True:
    run_circle()
    run_rectangle()
    
    break

CIRCLE
RECTANGKE
while True:
    # run_circle()
    run_rectangle()
    
    break

RECTANGKE
def run_rectangle():
    print("RECTANGKE")
    # Bottom line
    for x in range(50, 750+1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.01)

    for x in range(750, 50, -10):
    
    passRECTANGKE
    
SyntaxError: expected an indented block after 'for' statement on line 10
def render_all()
SyntaxError: expected ':'
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

    #for x in range(750, 50, -10)
    
    pass



RECTANGLE
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    RECTANGLE
NameError: name 'RECTANGLE' is not defined
def run_rectangle():
    print("RECTANGKE")
    # Bottom line
    for x in range(50, 750+1, 10):
        render_all(x, 90)

    for x in range(750, 50, -10)
        render_all(x, 550)
    pass
SyntaxError: expected ':'
def run_rectangle():
    print("RECTANGKE")
    # Bottom line
    for x in range(50, 750+1, 10):
        render_all(x, 90)

    for x in range(750, 50, -10):
        render_all(x, 550)
    pass

print("RECTANGLE")
RECTANGLE
while True:
    run_circle()
    run_rectangle()
    
    break

CIRCLE
RECTANGKE


while True:
    #run_circle()
    run_rectangle()
    
    break

RECTANGKE
while True:
    #run_circle()
    run_rectangle()
    
    break

RECTANGKE
def run_rectangle():
    print("RECTANGKE")
    # Bottom line
    for x in range(50, 750+1, 10):
        render_all(x, 90)
    #top line
    for x in range(750, 50-1, -10):
        render_all(x, 550)

    #for x in range (750, 50-1, -10):
    pass

while True:
    #run_circle()
    run_rectangle()
    
    break

RECTANGKE
while True:
    #run_circle()
    run_rectangle()
    
    break

RECTANGKE
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

    #for x in range (750, 50-1, -10):
    pass

while True:
    #run_circle()
    run_rectangle()
    
    break

RECTANGKE
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

while True:
    #run_circle()
    run_rectangle()
    
    break

RECTANGKE
while True:
    run_circle()
    run_rectangle()
    
    #break

    
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE
CIRCLE
RECTANGKE

