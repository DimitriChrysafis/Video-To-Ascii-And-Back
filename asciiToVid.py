import os
import pygame
import time

def print_ascii_image(file_path, screen):
    with open(file_path, 'r') as file:
        y = 0
        for line in file:
            font = pygame.font.SysFont(None, 24)
            text = font.render(line.rstrip('\n'), True, (255, 255, 255))
            screen.blit(text, (0, y))
            y += 24  # Increase the position for the next line

        pygame.display.flip()

def main():
    directory = "YOUR VIDEO PATH HERE"
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ASCII Video Player")

    clock = pygame.time.Clock()

    files = os.listdir(directory)
    files.sort()

    for file_name in files:
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            print_ascii_image(file_path, screen)
            time.sleep(0.1)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        clock.tick(120)  # FPS

    pygame.quit()

if __name__ == "__main__":
    main()
