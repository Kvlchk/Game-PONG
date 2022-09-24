from pygame import *
class GamesSPrite(sprite.Sprite):
    def __init__(self,player_image,plaeyr_x,player_y,player)speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.het_rect()
        self.rect.x = plaeyr_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

width = 600
height = 500
fon = (200,200,100)
window = display.set_mode((width,height))
window.fill(fon)
clock = time.Clock()
FPS = 60
ball = GameSprite("yball.png",200,200,4,50,50)
racket1 = Player("lplat.png",30,200,4,50,150)
racket2 = Player("rplat.png",520,200,,4,50,150)
game = True
finish = False
speed_x = 3
speed_y = 3
font.init()
font = font.FONT(None,35)
win2 = font.render("Player Right WIN!",TRUEE,(180,0,0)
win1 = font.render("Player Left WIN!",TRUEE,(180,0,0)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish !+ True:
        window.fill(fon)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1,ball) or (racket2,ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(win2,(200,200))
            game = True
        if ball.rect.x > 600:
            finish = True
            window.blit(win1(200,200))
            game = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
