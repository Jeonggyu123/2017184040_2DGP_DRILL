import game_framework
import play_state


def exit():
    global image
    del image

    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    draw_world()
    update_canvas()

def handleevents():
    events = get_events()
    for event in events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAOE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_state.boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    play_state.boy.item = 'BigBall'
                    game_framework.pop_state()




def draw_world():
    grass.draw()
    boy.draw()

def pause():
    pass

def resume():
    pass