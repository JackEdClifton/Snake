
# modules
import pygame, threading, winsound
pygame.init()

# objects
from game_class import Game_Class
game = Game_Class()

# mainloop
while game.run:

    # update display
    pygame.display.update()
    game.display.fill(game.bg)
    game.clock.tick(game.fps)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: game.run = False

        if event.type == pygame.KEYDOWN:
            # x axis
            if game.snake.direction in ["up", "down"]:
                if event.key == pygame.K_a:
                    game.snake.direction_queue = "left"
                elif event.key == pygame.K_d:
                    game.snake.direction_queue = "right"
            # y axis
            if game.snake.direction in ["left", "right"]:
                if event.key == pygame.K_w:
                    game.snake.direction_queue = "up"
                elif event.key == pygame.K_s:
                    game.snake.direction_queue = "down"
            
            if event.key == pygame.K_p:
                game.paused = not game.paused
            if event.key == pygame.K_f:
                game.toggle_display()
    
    # draw
    game.draw_map()
    game.draw_hud()
    game.snake.draw()
    game.snake.draw_food()
    if not game.paused:
        game.snake.move()
        game.snake.eat_food()
        game.snake.check_collision()

pygame.quit()
quit()

