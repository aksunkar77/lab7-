import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE, RED = (255, 255, 255), (255, 0, 0)

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_radius, step = 25, 20

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * step
    ball_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * step

    ball_x = max(ball_radius, min(WIDTH - ball_radius, ball_x))
    ball_y = max(ball_radius, min(HEIGHT - ball_radius, ball_y))

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

pygame.quit()
