Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pico2d
Pico2d is prepared.
pico2d.open_canvas()
pico2d.hide_lattice()
pico2d.show_lattice()
pico2d.close_canvas()
pico2d.open_canvas(1280, 720)
pico2d.close_canvas()
pico2d.open_canvas()
img = pico2d.load_image('character.png')
cannot load character.png
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    img = pico2d.load_image('character.png')
  File "C:\Python\lib\site-packages\pico2d\pico2d.py", line 349, in load_image
    raise IOError
OSError
import os
os.getcwd()
'C:\\Python'
os.chdir('c:/MyRepo/2017184040_2DGP_DRILL/Homework06')
os.getcwd()
'c:\\MyRepo\\2017184040_2DGP_DRILL\\Homework06'
os.listdir()
['.gitattributes', '.gitignore', 'character.png', 'character_grass.py', 'grass.png']
img = pico2d.load_image('character.png')
img.draw_now(400, 300)
img.draw_mow(800, 600)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    img.draw_mow(800, 600)
AttributeError: 'Image' object has no attribute 'draw_mow'. Did you mean: 'draw_now'?
img.draw_now(800, 600)
for x in range(0, 9):
    for y in range (0, 7):
        image.draw_now(x * 100, y * 100)

        
Traceback (most recent call last):
  File "<pyshell#22>", line 3, in <module>
    image.draw_now(x * 100, y * 100)
NameError: name 'image' is not defined
clear_canvas_now()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    clear_canvas_now()
NameError: name 'clear_canvas_now' is not defined
img.draw_now(400,400)
