import pygame

from classes.TextPost import TextPost
from helpers import screen, mouse_in_button, draw_comment_text_box, read_comment_from_user
from classes.ImagePost import ImagePost
from buttons import *
from classes.Comments import Comments


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    post_image = ImagePost("Nitzan", "Tel Aviv", "This is a test", 0, [], "Images/noa_kirel.jpg")
    post_image1 = ImagePost("Nitzan", "Tel Aviv", "this is a test", 0, [], "Images/ronaldo.jpg")

    new = TextPost("Nitzan", "Tel Aviv", "This is a test", 0, [], "This is a test", (255, 0, 0), BLACK)
    posts = [post_image, post_image1, new]
    running = True
    count = 0
    while running:
        current = posts[count % 3]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, mouse_pos):
                    current.likes_counter += 1
                if mouse_in_button(comment_button, mouse_pos):
                    text = read_comment_from_user()
                    comment = Comments(text)
                    current.comments.append(comment)
                    draw_comment_text_box()
                if mouse_in_button(click_post_button, mouse_pos):
                    count += 1
                if mouse_in_button(view_more_comments_button, mouse_pos):
                    pass

        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current.display()
        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    quit()


main()
