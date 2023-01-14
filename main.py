import pygame as pyg , random as rand , sys , time
from pygame.locals import *


screen_size = [600,600]

pyg.init()

display = pyg.display.set_mode(screen_size)
pyg.display.set_caption('snake game')



class snake:
    def __init__(self,x,y,w,h,color): # x -ray , y-ray , width , height,color of the snake
        self.x,self.y = x,y
        self.width,self.height = w,h
        self.color = color
        self.directions = {'right':True,'left':False,'up':False,'down':False}
    def update(self,keypressed):
        snak = pyg.draw.rect(display, self.color, [self.x,self.y,self.width,self.height])
        if keypressed[K_RIGHT]:
            for direction in self.directions:
                if direction == 'right':
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False
        elif keypressed[K_LEFT]:
            for direction in self.directions:
                if direction == 'left':
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False
        elif keypressed[K_UP]:
            for direction in self.directions:
                if direction == 'up':
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False
        elif keypressed[K_DOWN]:
            for direction in self.directions:
                if direction == 'down':
                    self.directions[direction] = True
                else:
                    self.directions[direction] = False
        
        if self.directions['right']:
            snak.x +=1
        elif self.directions['left']:
            snak.x -=1
        elif self.directions['up']:
            self.y -=1
        elif self.directions['down']:
            self.y +=1

# why i called this object snak cuz our class name is snake
snak= snake(screen_size[0]//2, screen_size[1]//2, 20, 20, 'green')

fps = 60
timer = pyg.time.Clock()

running = True
while running:
    timer.tick(fps)
    display.fill([0,0,0]) 
    for event in pyg.event.get():
        if event.type == QUIT:
            running = False
    keypressed = pyg.key.get_pressed()
    snak.update(keypressed)
    pyg.display.update()

pyg.quit()