from classes.Post import Post
from constants import *
import pygame

from helpers import screen


class ImagePost(Post):

    def __init__(self, username, location, description, likes_counter, comments, image_path):
        super().__init__(username, location, description, likes_counter, comments)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))

    def display(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        super().display()
