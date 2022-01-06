# -*- coding: utf-8 -*-
"""

@author: msran
"""

import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
#faster to use local font file than using a system  font
font = pygame.font.Font('arial.ttf', 25)




class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20
SPEED = 100

#RGB colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
COLOR1 = (16, 109, 255)
COLOR2 = (200, 100, 255)


class SnakeGameAI:
    
    def __init__(self, w = 640, h = 480):
        self.w = w
        self.h = h
        
        #init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()
        
        
    def reset(self):
        #init game state
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head, Point(self.head.x - BLOCK_SIZE, self.head.y), 
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]   
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0
        
        
    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()
            
    def play_step(self, action):
        self.frame_iteration += 1
        # Collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
            """
                    
        
        #move snake and update head
        
        self._move(action)
        self.snake.insert(0, self.head)
        
        #check if game over
        reward = 0
        game_over = False
        if self.collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score
        
        #place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        #update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        
        #return game over and score
        return reward, game_over, self.score
    
    def _update_ui(self):
        self.display.fill(BLACK)   
        for pt in self.snake:
            pygame.draw.rect(self.display, COLOR1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, COLOR2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))
        
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        
    def _move(self, action):
        #[straight, right,left]
        
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)
        
        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            
            #right turn r -> d -> l -> u
            new_dir = clock_wise[next_idx]
        else:
            #[0, 0, 1]
            next_idx = (idx - 1) % 4
            
            #left turn r -> u -> l -> d
            new_dir = clock_wise[next_idx]
        
        self.direction = new_dir
        
        x = self.head.x
        y = self.head.y
        
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE 
            
        self.head = Point(x, y)
        
    def collision(self, pt = None):
        
        if pt is None:
            pt = self.head
        #check if snake hits boundaries
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        
        #check if snake hits itself
        if pt in self.snake[1:]:
            return True
        
        return False
     
"""
if __name__ == "__main__":
    game = SnakeGameAI()
    
    #game loop
    while True:
        game_over, score = game.play_step()
        if game_over == True:
            break
        
        #print('Final Score ', score)
        
        
        #break whnn game over
        
        
    pygame.quit()
"""
