import pygame
from pygame.locals import *
import sys
import time

from button import *


def result(c_grade,score):

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
    if c_grade <= 1:
        grade = pygame.image.load('images/A.jpeg').convert_alpha()
    elif c_grade == 1.5:
        grade = pygame.image.load('images/D.jpeg').convert_alpha()
    elif c_grade == 2.0:
        grade = pygame.image.load('images/D.jpeg').convert_alpha()
    elif c_grade == 2.5:
        grade = pygame.image.load('images/c.jpeg').convert_alpha()
    elif c_grade == 3.0:
        grade = pygame.image.load('images/c+.jpeg').convert_alpha()
    elif c_grade == 3.5:
        grade = pygame.image.load('images/B.jpeg').convert_alpha()
    elif c_grade == 4.0:
        grade = pygame.image.load('images/B+.jpeg').convert_alpha()
    else:
        grade = pygame.image.load('images/A_+.jpeg').convert_alpha()
    grade =  pygame.transform.scale(grade, (240, 240))

    choice_size = (250, 80)
    oRetry = Button(screen, (WIDTH//2, HEIGHT*6.5//10), 'images/retry.png', 'images/retry_down.png', size = choice_size)
    oExit = Button(screen, (WIDTH//2, HEIGHT*8//10), 'images/exit.png', 'images/exit_down.png', size = choice_size)

    # Game loop
    runing = True
    while runing:

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
            return True
        if oExit.is_clicked():
            print("Exit Button Clicked!")
            time.sleep(0.3)
            return False
        # Update the screen
        pygame.display.flip()