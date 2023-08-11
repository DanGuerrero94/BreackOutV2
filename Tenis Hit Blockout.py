import pgzrun
import random

TITLE = "Tenis Hit Breakout"
WIDTH = 800
HEIGHT = 600

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 560

ball = Actor("ballgreen.png")
ball.x = 100
ball.y = 300

ball_x_speed = 3
ball_y_speed = 3

bars_list = []
score = 0
lvl_win = False
game_over = False

def draw():
    screen.blit("background.png", (0,0))
    if game_over:
        screen.draw.text('Game Over', (280, 300), color=(255,255,255), fontsize=50)
        screen.draw.text('Puntaje: ' + str(score), (280, 350), color=(255,255,255), fontsize=40)
    if lvl_win:
        screen.draw.text('Nivel Terminado', (280, 300), color=(255,255,255), fontsize=50)
        screen.draw.text('Puntaje: ' + str(score), (280, 350), color=(255,255,255), fontsize=40)    
    paddle.draw()
    ball.draw()
    screen.draw.text('Puntaje: ' + str(score), (15,10), color=(173,255,47), fontsize=25)

    for bar in bars_list:
        bar.draw()


def place_bars(x,y,image):
    bar_x = x
    bar_y = y
    for i in range(16):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 40
        bars_list.append(bar)

def update():
    global ball_x_speed, ball_y_speed, score, lvl_win, game_over
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5
    if (paddle.x <=60):
        paddle.x = 60
    if (paddle.x >=740):
        paddle.x = 740

    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
            score = score + 1
        if score >= 128:
            lvl_win = True
            ball_x_speed = 0
            ball_y_speed = 0
        if ball.y >= 580:
            game_over = True
            ball_x_speed = 0
            ball_y_speed = 0

    if paddle.colliderect(ball):
        ball_y_speed *= -1
        # randomly move ball left or right on hit
        rand = random.randint(0,1)
        if rand:
            ball_x_speed *= -1 

def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <=0):
        ball_x_speed *= -1
    if (ball.y >= HEIGHT) or (ball.y <=0):
        ball_y_speed *= -1

coloured_box_list = ["element_blue.png", "element_light_blue.png","element_grey.png","element_purple.png","element_yellow.png","element_orange.png","element_red.png","element_green.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 20
pgzrun.go()