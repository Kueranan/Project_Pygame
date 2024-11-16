import pygame
from pygame.locals import *
import sys

from button import *


def result():

    pygame.init()

    WIDTH = 720
    HEIGHT = 720
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Result')

    background = pygame.image.load('images/night.jpeg').convert_alpha()
    background =  pygame.transform.scale(background, (WIDTH, HEIGHT))
    rect_surface = pygame.Surface((720, 720), pygame.SRCALPHA)  
    rect_color = (102, 102, 102, 150)
    pygame.draw.rect(rect_surface, rect_color, pygame.Rect(0, 0, 620, 620), border_radius=10)
    grade = pygame.image.load('images/A.jpeg').convert_alpha()
    grade =  pygame.transform.scale(grade, (240, 240))

    choice_size = (250, 80)
    oRetry = Button(screen, (WIDTH//2, HEIGHT*6.5//10), 'images/retry.png', 'images/retry_down.png', size = choice_size)
    oExit = Button(screen, (WIDTH//2, HEIGHT*8//10), 'images/exit.png', 'images/exit_down.png', size = choice_size)

    # Game loop
    run = True
    while run:

        clock.tick(60)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

        screen.fill(0)

        screen.blit(background, background.get_rect())
        screen.blit(rect_surface, (50, 50))
        screen.blit(grade, (WIDTH//2-120,125))
        oRetry.draw()
        oExit.draw()

        if oRetry.is_clicked():
            print("Retry Button Clicked!")
        if oExit.is_clicked():
            print("Exit Button Clicked!")
            run = False

        # Update the screen
        pygame.display.flip()

result()

pygame.quit()
sys.exit()

