from pygame import *
width = 600
height = 500
fon = (200,200,100)
window = display.set_mode((win_width,win_height))
window.fill(fon)
clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
