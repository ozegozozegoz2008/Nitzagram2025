import pygame
from constants import *

class Post:
    def __init__(self, username, location, description, likes_counter, comments):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = likes_counter
        self.comments = comments
        self.comments_display_index = 0

    def display(self, img_path, size=(POST_WIDTH, POST_HEIGHT), pos=(POST_X_POS, POST_Y_POS)):
        image = pygame.image.load(img_path)
        image = pygame.transform.scale(image, size)
        screen.blit(image, pos)

    def display_comments(self):
        position_index = self.comments_display_index
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments", True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))
        for i in range(NUM_OF_COMMENTS_TO_DISPLAY):
            if position_index >= len(self.comments):
                position_index = 0

            comment_font = pygame.font.SysFont('name', COMMENT_TEXT_SIZE)
            comment_text = comment_font.render(self.comments[position_index], True, BLACK)
            comment_y_pos = FIRST_COMMENT_Y_POS + (i * COMMENT_LINE_HEIGHT)
            screen.blit(comment_text, (FIRST_COMMENT_X_POS, comment_y_pos))

            position_index += 1

    def update_comments_index(self, direction):
        """
        Update the comments_display_index to show the next or previous set of comments.

        :param direction: The direction to scroll ('next' or 'previous')
        :return: None
        """
        if direction == 'next':
            if self.comments_display_index + NUM_OF_COMMENTS_TO_DISPLAY < len(self.comments):
                self.comments_display_index += NUM_OF_COMMENTS_TO_DISPLAY
        elif direction == 'previous':
            if self.comments_display_index - NUM_OF_COMMENTS_TO_DISPLAY >= 0:
                self.comments_display_index -= NUM_OF_COMMENTS_TO_DISPLAY


pygame.init()

screen = pygame.display.set_mode((800, 600))

comments = [
    "Great post!",
    "I agree, amazing!",
    "This is so true!",
    "I love this content!",
    "More posts like this please!",
    "Keep it up!",
    "This is awesome!",
    "Incredible, I am a fan!"
]

post = Post("User123", "LocationXYZ", "This is a great post!", 100, comments)

running = True
while running:
    screen.fill((255, 255, 255))

    post.display("path_to_image.jpg")
    post.display_comments()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                post.update_comments_index('next')
            elif event.key == pygame.K_UP:
                post.update_comments_index('previous')

    pygame.display.flip()

pygame.quit()
