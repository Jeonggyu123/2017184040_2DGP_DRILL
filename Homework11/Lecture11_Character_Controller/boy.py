import pico2d
from pico2d import *

# 이벤트 정의
#RD, LD, RU, LU = 0, 1, 2, 3  # right down, left down, right up, left up
RD, LD, RU, LU, TIMER, AR = range(6) #위와 의미는 동일 #타이머 추가

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT)  : LD,
    (SDL_KEYUP, SDLK_RIGHT)   : RU,
    (SDL_KEYUP, SDLK_LEFT)    : LU,
    (SDL_KEYDOWN, SDLK_a)     : AR
} # 단순화 맵핑? 키입력을 단일이벤트로 만들기 위해서

global a

# 스테이트를 구현 - 클래스를 이용해서..
class IDLE:
    @staticmethod   # c++에서 클래스안에 스태틱선언한 것과 비슷(self생략)
    def enter(self, event): #어떤 이벤트로 인해 들어왔는지 확인하기위해 event필요
        print('ENTER IDLE')
        self.dir = 0 # 정지 상태
        self.timer = 1000 #타이머 초기화
        pass

    @staticmethod
    def exit(self):
        print('EXIT IDLE')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1 # 시간 감소
        if self.timer == 0: #시간이 다 되면
            self.add_event(TIMER) # 타이머 이벤트를 큐에 삽입
        pass

    @staticmethod
    def draw(self):

        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        # elif self.a == 1:
        #     self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        pass

class RUN:
    def enter(self, event): #
        print('ENTER RUN')

        # 어떤 이벤트때문에, RUN으로 들어왔는지 파악을 하고, 그 이벤트를 따라서 실제방향을 결정.
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

        pass

    def exit(self):
        print('ENTER RUN')
        #런 상태를 나갈 때, 현재 방향을 저장해놓음.
        self.face_dir = self.dir
        pass

    def do(self):
        # 달리게 만들어 준다.
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800) # clamp
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class AUTO_RUN: # 자동 무적 런
    @staticmethod  # c++에서 클래스안에 스태틱선언한 것과 비슷(self생략)
    def enter(self, event):  # 어떤 이벤트로 인해 들어왔는지 확인하기위해 event필요
        print('ENTER IDLE')
        if event == AR:
            self.a = 1
        self.dir = 0  # 정지 상태
        pass

    @staticmethod
    def exit(self):
        self.face_dir = self.dir
        print('EXIT IDLE')
        pass

    @staticmethod
    def do(self):
        self.autorun(a == 1)
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):

        if self.a == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y, 300, 300)
        pass



class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0 # 정지 상태
        pass

    @staticmethod
    def exit(self):
        print('EXIT SLEEP')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):

        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2, '',
                                           self.x+25, self.y-25, 100, 100)
            #clip_composite_draw(left, bottom, height, rad, flip, x, y, w, h)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592/2, '',
                                           self.x-25, self.y-25, 100, 100)

        pass

# 상태 변환

#상태변환 테이블
next_state = {
    SLEEP: { RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, },
    IDLE : { RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP },  #동시에 누를 때도 RUN
    RUN  : { RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, TIMER:RUN }
}



class Boy:

    def handle_event(self, event): #event : 키 입력 이벤트
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) #ctrl + / 커맨드 아웃



    def add_event(self, key_event):
        self.q.insert(0, key_event)

    # def handle_event(self, event): #boy에 핸들 이벤트 넣기
    #     if event.type == SDL_KEYDOWN:
    #         match event.key:
    #             case pico2d.SDLK_LEFT:
    #                 self.dir -= 1
    #             case pico2d.SDLK_RIGHT:
    #                 self.dir += 1
    #     elif event.type == SDL_KEYUP:
    #         match event.key:
    #             case pico2d.SDLK_LEFT:
    #                 self.dir += 1
    #                 self.face_dir = -1
    #             case pico2d.SDLK_RIGHT:
    #                 self.dir -= 1
    #                 self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []

        #초기 상태 설정과, entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        #self.cur_state = AUTO_RUN



    # 오토 런
    def autorun(self, event):
        if self.event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_a:
                    self.AUTO_RUN.a = 1
            self.pico2d.scale += 10

        pass





    def update(self):
        self.cur_state.do(self)
        #self.autorun.do(self)

        if self.q: #만약에 list q 에 뭔가 들어있으면
            event = self.q.pop() #이벤트를 확인하고,
            self.cur_state.exit(self) # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event] #다음상태 계산
            self.cur_state.enter(self, event) #다음 상태의 enter 액션을 수행

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)
        #self.autorun.draw(self)


