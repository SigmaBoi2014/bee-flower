import pgzrun
import random

WIDTH=500
HEIGHT=400
score=0
game_over=False
spider=Actor("spiderman (2)")
spider.pos = 100,100
venom =Actor("venom (1)")
venom.pos = 200,200
def update():
    global score
    if (keyboard.left):
        spider.x=spider.x -2
    if (keyboard.right):
        spider.x = spider.x +2
    if (keyboard.up):
        spider.y=spider.y-2
    if(keyboard.down):
        spider.y=spider.y+2
    venom_collected=spider.colliderect(venom)
    if venom_collected:
        score=score+10
        place_venom()
def place_venom():
    venom.x=random.randint(10,(WIDTH-10))
    venom.y=random.randint(10,(HEIGHT-10))
def time_up():
    global game_over
    game_over=True
def draw():
    screen.blit("newyork",(0,0))
    spider.draw()
    venom.draw()
    screen.draw.text("score:"+str(score),color="blue",topleft=(10,10))
    if game_over:
        screen.fill("black")
        screen.draw.text("Time's up! Your Final Score:"+str(score),midtop=(WIDTH/2,10),fontsize=40,color="red")
clock.schedule(time_up,60.0)
pgzrun.go()