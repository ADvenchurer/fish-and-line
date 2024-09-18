import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

fishes = []
lines = []
next_fish = 0

start_time = 0
total_time = 0
end_time = 0

number_of_fishes = 8

def create_fishes():
    global start_time
    for count in range(0,number_of_fishes):
        fish = Actor("fish")
        fish.pos = randint(40,WIDTH-40), randint(40,HEIGHT-40)
        fishes.append(fish)
    start_time = time()


def draw():
    global total_time
    screen.blit("water", (0,0))
    number = 1
    for fish in fishes:
        screen.draw.text(str(number), (fish.pos[0], fish.pos[1]+20))
        fish.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_fish < number_of_fishes:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

def update():
    pass

def on_mouse_down(pos):
    global next_fish, lines

    if next_fish < number_of_fishes:
        if fishes[next_fish].collidepoint(pos):
            if next_fish:
                lines.append((fishes[next_fish-1].pos,fishess[next_fish].pos))
            next_fish = next_fish + 1
        else:
            lines = []
            next_fish = 0

create_fishes()

pgzrun.go()