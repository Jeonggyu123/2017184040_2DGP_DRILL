from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

#def idle_events():


def handle_events():
    # fill here
    global running
    global dirX, dirY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_DOWN:
                dirY += 1
            elif event.key == SDLK_UP:
                dirY -= 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0

framey = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()

    frame = (frame + 1) % 8
    if dirX-x<0:
        framey = 0
    else :
        framey = 1


    x += dirX * 5
    y += dirY * 5
    delay(0.05)

    handle_events()

close_canvas()