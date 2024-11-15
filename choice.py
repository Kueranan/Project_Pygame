import pygame
from pygame.locals import *

class Choice:
    def __init__(self, screen, pos, up_image, down_image, font_size, text, size = None):
        self.screen = screen
        self.image_up = pygame.image.load(up_image).convert_alpha()
        self.image_down = pygame.image.load(down_image).convert_alpha()

        if size:
            self.image_up = pygame.transform.scale(self.image_up, size)
            self.image_down = pygame.transform.scale(self.image_down, size)

        self.image = self.image_up
        self.rect = self.image.get_rect(center = pos)
        self.font = pygame.font.Font('k2d/K2D-Light.ttf', font_size)
        self.text = self.font.render(text, True, (0, 0, 0))
        self.texttile = self.text.get_rect(center=self.rect.center)
        self.clicked = False

    def draw(self):
        self.texttile = self.text.get_rect(center=self.rect.center)

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.texttile)

    def is_clicked(self):
        # Check if button is clicked
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
