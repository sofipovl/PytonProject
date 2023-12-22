import pygame
import sys

pygame.init()

win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))

background_image = pygame.image.load("menu.png")
background_image = pygame.transform.scale(background_image, (win_width, win_height))

white = (40, 150, 200)
black = (0, 0, 0)

font = pygame.font.Font('Realest-Extended.otf', 20)


class Button:
    def __init__(self, x, y, width, height, color, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            text = font.render(self.text, 1, black)
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


def main():
    new_game_button = Button(300, 150, 200, 50, white, 'New Game')
    quit_button = Button(300, 250, 200, 50, white, 'Quit')
    with_friend_button = Button(300, 350, 200, 50, white, 'With Friend')

    running = True
    while running:
        # Отрисовка изображения фона
        win.blit(background_image, (0, 0))

        new_game_button.draw(win, (0, 0, 0))
        quit_button.draw(win, (0, 0, 0))
        with_friend_button.draw(win, (0, 0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if new_game_button.isOver(pos):
                    pass
                if quit_button.isOver(pos):
                    running = False
                    pygame.quit()
                    sys.exit()
                if with_friend_button.isOver(pos):
                    pass


if __name__ == "__main__":
    main()
