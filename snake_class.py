import pygame; pygame.init()
import random


class Snake:

    def __init__(self, display):
        self.display = display

    
    def reset_game(self):
        self.length = 1
        self.position = []

        [self.position.append((x,260)) for x in range(40,81,2)]

        self.direction = "right"
        self.direction_queue = "right"
        self.direction_index = 0

        self.spawn_food()
        self.extend_by = 0
        self.colliding = False


    def draw(self):
        
        for body in self.position:
            pygame.draw.circle(self.display, (30,50,140), body, 10)

    

    def move(self):
        if self.extend_by == 0: self.position = self.position[1:]
        else: self.extend_by -= 1
        x,y = self.position[-1]
        if self.direction == "left": x -= 2
        if self.direction == "right": x += 2
        if self.direction == "up": y -= 2
        if self.direction == "down": y += 2

        self.position.append((x,y))

        self.direction_index += 1

        if self.direction_index == 10:
            self.direction = self.direction_queue
            self.direction_index = 0
    

    def spawn_food(self):
        x = random.choice(range(20,581,20))
        y = random.choice(range(80,521, 20))

        self.food_position = (x,y)
    
 
    def draw_food(self):
        pygame.draw.circle(self.display, (180,40,40), (self.food_position), 8)
    

    def eat_food(self):
        head = self.position[-1]
        if head == self.food_position:
            self.spawn_food()
            self.length += 1
            self.extend_by += 5
    

    def check_collision(self):

        self.colliding = False
        head = self.position[-1]
        # collide with it self
        for body in self.position[:-1]:
            if body == head: self.colliding = True

        # collide with wall
        if not(head[0] in range (20,581) and head[1] in range(70,590)): self.colliding = True


