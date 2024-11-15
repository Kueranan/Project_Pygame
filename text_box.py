import pygame
from pygame.locals import *

class TextBox():
    def __init__(self, screen, width, height, position, text, font_size=40, color=(102, 102, 102, 225), text_color=(225, 225, 225), transparency=0.75):
        
        self.screen = screen
        self.width = width
        self.height = height
        self.x, self.y = position
        self.color = (color[0], color[1], color[2], int(225 * transparency))
        self.text = text
        self.text_color = text_color

        self.rect_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.font = pygame.font.Font('k2d/K2D-Bold.ttf', font_size)
        
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_x = (self.width - self.text_surface.get_width()) // 2
        self.text_y = (self.height - self.text_surface.get_height()) // 2

    def draw(self):

        self.rect_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(self.rect_surface, self.color, pygame.Rect(0, 0, self.width, self.height), border_radius=10)
        self.rect_surface.blit(self.text_surface, (self.text_x, self.text_y))
        self.screen.blit(self.rect_surface, (self.x, self.y))
