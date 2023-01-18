import pygame as pyg , sys, random ,time
from pygame.locals import *


frame_size_x = 720
frame_size_y = 480

pyg.init()
display = pyg.display.set_mode((frame_size_x,frame_size_y))
pyg.display.set_caption('snake')

food_pos = [random.randrange(0,frame_size_x//10 *10),random.randrange(0,frame_size_y//10 *10)]

# game variables
score = 0
x,y = 400,400
direction = 'right'
change_to = direction
speed = 3
fps_controller = 60
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
snake_pos = [100, 50]
timer = pyg.time.Clock()
while True:
    timer.tick(fps_controller)
    display.fill([0,0,0])
    food = pyg.draw.rect(display, [255,0,0], [food_pos[0],food_pos[1],10,10])
    for pos in snake_body:
        snake = pyg.draw.rect(display, [255,255,255], [pos[0],pos[1],10,10])
    snake_body.insert(0, list(snake_pos))
    snake_body.pop()
    # event handling 
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            sys.exit()
    key_pressed = pyg.key.get_pressed()

    if key_pressed[K_RIGHT]:
        direction = 'right'
    elif key_pressed[K_LEFT]:
        direction = 'left'
    elif key_pressed[K_UP]:
        direction = 'up'
    elif key_pressed[K_DOWN]:
        direction = 'down'
    change_to = direction

    if change_to == 'right':
        snake_pos[0]+=speed
    elif change_to == 'left':
        snake_pos[0]-=speed
    elif change_to == 'down':
        snake_pos[1]+=speed
    elif change_to == 'up':
        snake_pos[1]-=speed
    

    if food_pos[0] >= snake_pos[0] and snake_pos[0] <= food_pos[0] and  snake_pos[1] <= food_pos[1] and food_pos[1] >= snake_pos[1]:
        score+=1
        print(score)
        food_pos = [random.randrange(0,frame_size_x//10 *10),random.randrange(0,frame_size_y//10 *10)]
        snake_body.insert(0, list(snake_pos))

    pyg.display.update()