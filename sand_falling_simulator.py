# import the pygame module
import pygame
from time import sleep
import threading

# Constants
WIDTH = 625
HEIGHT = 625
SAND_COLOR = (230, 164, 180)
BACKGROUND_COLOR = (253, 240, 209)
SAND_HEIGHT = 25
SAND_WIDTH = 25
JUMP = WIDTH//SAND_WIDTH


def on_click(screen, pos):
    pygame.draw.rect(screen, SAND_COLOR,
                     pygame.Rect((pos[0] // JUMP) * JUMP, (pos[1] // JUMP) * JUMP, SAND_HEIGHT, SAND_WIDTH))
    for i in range(HEIGHT // JUMP - (pos[1] // JUMP) - 1):
        if screen.get_at(((pos[0] // JUMP) * JUMP, (pos[1] // JUMP + i + 1) * JUMP)) == SAND_COLOR:
            break
        pygame.draw.rect(screen, SAND_COLOR,
                         pygame.Rect((pos[0] // JUMP) * JUMP, (pos[1] // JUMP + i + 1) * JUMP, SAND_HEIGHT,
                                     SAND_WIDTH))
        pygame.draw.rect(screen, BACKGROUND_COLOR,
                         pygame.Rect((pos[0] // JUMP) * JUMP, (pos[1] // JUMP + i) * JUMP, SAND_HEIGHT,
                                     SAND_WIDTH))
        sleep(0.01)
        pygame.display.flip()



def main():
    arr_size = HEIGHT//SAND_HEIGHT
    arr = [[0 for _ in range(arr_size)] for _ in range(arr_size)]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('sand falling simulation!')
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    running = True

    # game loop
    while running:
        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
            # Main stuff
            sleep(0.03)
            pos = pygame.mouse.get_pos()
            curr_thread = threading.Thread(target=on_click, args=(screen, pos,))
            curr_thread.start()
            pygame.display.flip()


if __name__ == "__main__":
    main()
