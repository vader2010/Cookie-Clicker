import pygame
from pygame import *

pygame.init()
X = 1920
Y = 1080
app = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)
cursor = pygame.image.load("cursor.png").convert_alpha()
def draw_cursors(row, cursors, rotation_offset):
    y_increase = (10 * row) + 10
    space_in_between = 5 * row
    for i in range(0,  len(str(cursors))):
        rotated_image = pygame.transform.rotate(cursor, (7.2*i)  + rotation_offset)
        print(i)
        app.blit(rotated_image, (0, 0))
        
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
            coordinates = pygame.mouse.get_pos()
            offset_x = coordinates[0] - 50
            offset_y = coordinates[1] - 270
            if cookie_mask.overlap(clicker_mask, (offset_x, offset_y)):
                if cookie_clicked > 5:
                    cookies1 += 1
                    cookie_clicked = 0
        elif not pygame.mouse.get_pressed()[0] and clicking:
            clicking = False
        cookies_str = str(cookies1)
        endings = ["million", "billion", "trillion", "quadrillion"]
        ending_str = None
        for i in range(len(endings)):
            if len(cookies_str) > (6 + (i * 3)):
                ending = endings[i]
                ending_str = f"{endings[i]} cookies"
        app.blit(cookie_scaled, (50, 270))
        app.blit(clicker, coordinates)
        if cookies1 == 0:
            cookies2 = kavoon_font.render(f"0 cookies", True, (255, 255, 255))
        elif cookies1 == 1:
            cookies2 = kavoon_font.render(f"1 cookie", True, (255, 255, 255))
        elif cookies1 > 999999:
            cookies2 = kavoon_font.render(f"{cookies_str[0]}.{cookies_str[1:3]} {ending_str}", True, (255, 255, 255))
        elif cookies1 < 1000000:
            cookies2 = kavoon_font.render(f"{cookies_str} cookies", True, (255, 255, 255))
        cookies_rect = cookies2.get_rect(center=(225, 75))
        app.blit(cookies2, cookies_rect)
        pygame.display.flip()

pygame.quit()
