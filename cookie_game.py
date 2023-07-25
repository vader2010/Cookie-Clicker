import pygame
from pygame import *

pygame.init()
X = 1920
Y = 1080
app = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)
cookie = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Cookie Clicker\\cookie.png").convert_alpha()
kavoon_font = pygame.font.Font("Kavoon-Regular.ttf", 18)
cookie_scaled = pygame.transform.scale(cookie, (350, 350))
app.blit(cookie_scaled, (50, 270))
cookie_mask = pygame.mask.from_surface(cookie_scaled)
clicker = pygame.surface.Surface((10, 10))
clicker.fill((255, 0, 0))
clicker_mask = pygame.mask.from_surface(clicker)
pygame.display.flip()
running = True
cookies = 0
while running:
    for event in pygame.event.get():
        app.fill((0, 0, 0))
        coordinates = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if pygame.mouse.get_pressed()[0]:
            print('clicked')
            if clicker_mask.overlap(cookie_mask, (coordinates[0] - cookie_scaled.get_rect().x, coordinates[1] - cookie_scaled.get_rect().y)):
                print("run")
                cookies += 1
                print(cookies)
        app.blit(cookie_scaled,  (50, 270))
        app.blit(clicker, coordinates)
        pygame.display.flip()

pygame.quit()
