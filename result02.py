import pygame
from pygame.locals import *
import sys

from button import *


def result():

    pygame.init()

    WIDTH = 600
    HEIGHT = 600
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Result')

    background = pygame.image.load('images/night.jpeg').convert_alpha()
    background =  pygame.transform.scale(background, (WIDTH, HEIGHT))
    grade = pygame.image.load('images/A.jpeg').convert_alpha()
    grade =  pygame.transform.scale(grade, (200, 200))

    rect_surface = pygame.Surface((500, 500), pygame.SRCALPHA)  
    rect_color = (102, 102, 102, 150)
    pygame.draw.rect(rect_surface, rect_color, pygame.Rect(0, 0, 500, 500), border_radius=10)
    

    oRetry = Button(screen, (WIDTH//2, HEIGHT*6.5//10), 'images/retry.png', 'images/retry_down.png')
    oExit = Button(screen, (WIDTH//2, HEIGHT*8//10), 'images/exit.png', 'images/exit_down.png')

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
        screen.blit(grade, (WIDTH//2-100,125))
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

