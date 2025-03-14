import pygame
import time
import math
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
CENTER = (WIDTH // 2, HEIGHT // 2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
minute_hand = pygame.image.load("minute_hand.png")
second_hand = pygame.image.load("second_hand.png")
def draw_hand(image, angle, length):
    """Мики Маусын гарны байрлалыг бодож эргүүлж зурна"""
    rotated_hand = pygame.transform.rotate(image, angle)
    rect = rotated_hand.get_rect(center=(CENTER[0] + length * math.cos(math.radians(angle)),
                                         CENTER[1] - length * math.sin(math.radians(angle))))
    screen.blit(rotated_hand, rect.topleft)
def draw_clock_face():
    """Цагны хүрээ болон тоонуудыг зурна"""
    pygame.draw.circle(screen, BLACK, CENTER, 120, 5) 
    pygame.draw.circle(screen, BLACK, CENTER, 5)  
    for i in range(12):
        angle = math.radians(30 * i)
        x1 = CENTER[0] + 100 * math.cos(angle)
        y1 = CENTER[1] - 100 * math.sin(angle)
        x2 = CENTER[0] + 110 * math.cos(angle)
        y2 = CENTER[1] - 110 * math.sin(angle)
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 3)

running = True
while running:
    screen.fill(WHITE)
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    min_angle = 90 - (minutes * 6)
    sec_angle = 90 - (seconds * 6)
    draw_clock_face()
    draw_hand(minute_hand, min_angle, 70)  
    draw_hand(second_hand, sec_angle, 90)  
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
