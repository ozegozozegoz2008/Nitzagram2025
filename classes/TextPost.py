import pygame

from constants import *
from helpers import *
from Post import Post


class TextPost(Post):
    def __init__(self, username, location, description, likes_counter, comments, text, text_color, backround_color):
        super().__init__(username, location, description, likes_counter, comments)
        self.text_arr = from_text_to_array(text)
        self.text_color = text_color
        self.backround_color = backround_color

    def display(self):
        super().display()
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.backround_color, square)
        n = len(self.text_arr)
        for i in range(n):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text_arr[i], True, self.text_color)
            pos = center_text(n, text, i)
            screen.blit(text, pos)

