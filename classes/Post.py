import pygame

from constants import *
from helpers import *


class Post:
    def __init__(self, username, location, description, likes_counter, comments):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = likes_counter
        self.comments = comments
        self.comments_display_index = 0

    def display(self):
        self.display_username()
        self.display_location()
        self.display_description()
        self.display_likes()
        self.display_comments()

    def display_username(self):
        text_display(str(self.username), UI_FONT_SIZE, (USER_NAME_X_POS, USER_NAME_X_POS))

    def display_location(self):
        text_display(str(self.location), UI_FONT_SIZE, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

    def display_description(self):
        text_display(str(self.description), UI_FONT_SIZE, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

    def display_likes(self):
        text_display(str(self.likes_counter), UI_FONT_SIZE, (LIKE_TEXT_X_POS, LIKE_BUTTON_Y_POS))

    def display_comments(self):
        position_index = self.comments_display_index

        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments", True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))
        for i in range(NUM_OF_COMMENTS_TO_DISPLAY):
            if position_index >= len(self.comments):
                position_index = 0

            comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
            comment_text = comment_font.render(self.comments[position_index], True, BLACK)
            comment_y_pos = FIRST_COMMENT_Y_POS + (i * COMMENT_LINE_HEIGHT)
            screen.blit(comment_text, (FIRST_COMMENT_X_POS, comment_y_pos))

            position_index += 1

    def update_comments_index(self, direction):
        if direction == 'next':
            if self.comments_display_index + NUM_OF_COMMENTS_TO_DISPLAY < len(self.comments):
                self.comments_display_index += NUM_OF_COMMENTS_TO_DISPLAY
        elif direction == 'previous':
            if self.comments_display_index - NUM_OF_COMMENTS_TO_DISPLAY >= 0:
                self.comments_display_index -= NUM_OF_COMMENTS_TO_DISPLAY

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        self.comments.append(text)




