from helpers import *


class Comments:
    def __init__(self, comment):
        self.comment = comment
        self.font = pygame.font.SysFont('arial', COMMENT_TEXT_SIZE)
        self.text_surface = self.font.render(str(self.comment), True, BLACK)
        self.rect = self.text_surface.get_rect()

    def display(self, index):
        y_position = FIRST_COMMENT_Y_POS + (index * COMMENT_TEXT_SIZE)
        self.rect.topleft = (FIRST_COMMENT_X_POS, y_position)
        screen.blit(self.text_surface, self.rect)
        screen.blit(self.text_surface, self.rect)