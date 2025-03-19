import pgzrun
import random

WIDTH=500
HEIGHT=400
score=0
game_over=False
bee=Actor("bee")
bee.pos = 100,100
flower=Actor("flower")
flower.pos = 200,200
def update():
    global score
    if (keyboard.left):
        bee.x=bee.x -2
    if (keyboard.right):
        bee.x = bee.x +2
    if (keyboard.up):
        bee.y=bee.y-2
    if(keyboard.down):
        bee.y=bee.y+2
    flower_collected=bee.colliderect(flower)
    if flower_collected:
        score=score+10
        place_flower()
def place_flower():
    flower.x=random.randint(10,(WIDTH-10))
    flower.y=random.randint(10,(HEIGHT-10))
def time_up():
    global game_over
    game_over=True
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:"+str(score),color="blue",topleft=(10,10))
    if game_over:
        screen.fill("black")
        screen.draw.text("Time's up! Your Final Score:"+str(score),midtop=(WIDTH/2,10),fontsize=40,color="red")
clock.schedule(time_up,60.0)
pgzrun.go()
