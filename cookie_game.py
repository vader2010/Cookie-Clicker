import pygame
from pygame import *

pygame.init()
X = 1920
Y = 1080
app = pygame.display.set_mode((X, Y))
cookie = pygame.image.load("cookie.png").convert_alpha()
kavoon_font = pygame.font.Font("Kavoon-Regular.ttf", 32)
cookie_scaled = pygame.transform.scale(cookie, (350, 350))
app.blit(cookie_scaled, (50, 270))
cookie_mask = pygame.mask.from_surface(cookie_scaled)
clicker = pygame.surface.Surface((10, 10))
clicker.fill((255, 0, 0))
clicker_mask = pygame.mask.from_surface(clicker)
pygame.display.flip()
running = True
cookies1 = 0
cookie_clicked = 0
clicking = False
while running:
    cookie_clicked += 1
    for event in pygame.event.get():
        app.fill((0, 0, 0))
        coordinates = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if pygame.mouse.get_pressed()[0] and not clicking:
            clicking = True
            print('clicked')
            offset_x = coordinates[0] - 50
            offset_y = coordinates[1] - 270
            if cookie_mask.overlap(clicker_mask, (offset_x, offset_y)):
                if cookie_clicked > 5:
                    cookies1 += 1
                    cookie_clicked = 0
        elif not pygame.mouse.get_pressed()[0] and clicking:
            clicking = False
        app.blit(cookie_scaled, (50, 270))
        app.blit(clicker, coordinates)
        cookies2 = kavoon_font.render(f"Cookies: {cookies1}", True, (255, 255, 255))
        app.blit(cookies2, (0, 0))
        pygame.display.flip()


pygame.quit()
