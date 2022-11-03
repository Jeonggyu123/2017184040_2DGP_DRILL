# layer 0: Background Objects
# layer 1: Foreground Objects
world = [[], []]  #world list

def add_object(o, depth):   # 객체 하나추가
    world[depth].append(o)

def add_objects(ol, depth):     # 객체 여러개 추가
    world[depth] += ol

def remove_object(o):   #화면 밖을 나간 객체 사라지게하기
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o  # 실제로 메모리 삭제
            return
    raise ValueError('Trying destroy non existing object')
    #world.remove(o) #리스트로부터 삭제

def all_objects(): # 게임 월드의 모든 객체들을 하나씩 꺼내오기
    for layer in world:
        for o in layer:
            yield o

def clear(): # 게임 월드의 모든 객체 제거
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()