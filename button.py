import pygame
from pygame.locals import *

class Button:
    def __init__(self, screen, pos, up_image, down_image, size = None):
        self.screen = screen
        self.image_up = pygame.image.load(up_image).convert_alpha()
        self.image_down = pygame.image.load(down_image).convert_alpha()
        
        if size:
            self.image_up = pygame.transform.scale(self.image_up, size)
            self.image_down = pygame.transform.scale(self.image_down, size)
        
        self.image = self.image_up
        self.rect = self.image.get_rect(center=pos)
        self.clicked = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_down
            if mouse_pressed[0] and not self.clicked:
                self.clicked = True
                return True
        else:
            self.image = self.image_up
        
        if not mouse_pressed[0]:
            self.clicked = False
        
        return False
