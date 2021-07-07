
# modules
import pygame; pygame.init()
from snake_class import Snake
from time import sleep
from threading import Thread

class Game_Class:

    # setup
    def __init__(self):

        self.res = (600,600)
        self.fps = 60
        self.fullscreen = False
        self.bg = (100,120,200)

        self.run = True
        self.paused = False
        self.display = self.display = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()
        self.time_elasped = ("00","00")
        Thread(target=self.run_time).start()

        self.snake = Snake(self.display)
        self.snake.reset_game()

        self.font = pygame.font.Font("freesansbold.ttf", 32)



    # fullscreen
    def toggle_display(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen: self.display = pygame.display.set_mode(self.res)
        else: self.display = pygame.display.set_mode(self.res, pygame.FULLSCREEN)


    # map
    def draw_map(self):

        b = 3
        pygame.draw.rect(self.display, (0,50,0), (10-b,70-b,580+b*2,520+b*2))

        colours = [
            (90,170,90),
            (150,200,150),
        ]

        for y in range(26):

            if y % 2 == 0: index = False
            else: index = True

            for x in range(29):
                x_pos = 20*x + 10
                y_pos = 20*y + 70

                pygame.draw.rect(self.display, colours[index], (x_pos,y_pos,20,20))
                index = not index


    # hud
    def draw_hud(self):
        score = self.font.render("Score: "+str(self.snake.length), True, (0,0,0))
        time =  self.font.render("Time: "+":".join(self.time_elasped), True, (0,0,0))
        self.display.blit(score, (10,10))
        self.display.blit(time, (400,0))

        if self.paused:
            self.dim_screen()
        if self.snake.colliding:
            self.dim_screen()
            pygame.display.update()
            sleep(1)
            self.snake.reset_game()
    
    # time
    def run_time(self):
        m, s = self.time_elasped
        while True:
            m = int(m)
            s = int(s)
            s += 1
            if s == 60:
                m += 1
                s = 0
            if s < 10: s = f"0{str(s)}"
            self.time_elasped = (str(m),str(s))
            sleep(1)
            while self.paused:
                sleep(0.4)


    def dim_screen(self):
        fade = pygame.Surface(self.res)
        fade.fill((0,0,0))
        fade.set_alpha(100)

        self.display.blit(fade, (0,0))
