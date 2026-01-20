import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (10, 10, 10)
RED = (255, 0, 0)

font = pygame.font.SysFont('Arial', 10)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

thanh_truot = pygame.Rect(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT - 40, 100, 10)
ball = pygame.Rect(SCREEN_WIDTH / 2 - 15, 50, 30, 30)

ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 * random.choice((1, -1))

running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x = pygame.mouse.get_pos()[0]

    thanh_truot.centerx = mouse_x

    if thanh_truot.left <= 0:
        thanh_truot.left = 0
    if thanh_truot.right >= SCREEN_WIDTH:
        thanh_truot.right = SCREEN_WIDTH

    ball.x = ball.x + ball_speed_x
    ball.y = ball.y + ball_speed_y

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x

    if ball.colliderect(thanh_truot) or ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Drawing
    screen.fill(BLACK)

    text_xy = font.render('50', True, (255, 255, 255))  # White text
    text_rect = text_xy.get_rect(center=(50, 5))
    screen.blit(text_xy, text_rect)
    text_rect = text_xy.get_rect(center=(5, 50))
    screen.blit(text_xy, text_rect)

    text_xy = font.render('100', True, (255, 255, 255))  # White text
    text_rect = text_xy.get_rect(center=(100, 5))
    screen.blit(text_xy, text_rect)
    text_rect = text_xy.get_rect(center=(5, 100))
    screen.blit(text_xy, text_rect)

    text_xy = font.render('150', True, (255, 255, 255))  # White text
    text_rect = text_xy.get_rect(center=(150, 5))
    screen.blit(text_xy, text_rect)
    text_rect = text_xy.get_rect(center=(5, 150))
    screen.blit(text_xy, text_rect)

    text_xy = font.render('200', True, (255, 255, 255))  # White text
    text_rect = text_xy.get_rect(center=(200, 5))
    screen.blit(text_xy, text_rect)
    text_rect = text_xy.get_rect(center=(5, 200))
    screen.blit(text_xy, text_rect)

    text_xy = font.render('250', True, (255, 255, 255))  # White text
    text_rect = text_xy.get_rect(center=(250, 5))
    screen.blit(text_xy, text_rect)
    text_rect = text_xy.get_rect(center=(5, 250))
    screen.blit(text_xy, text_rect)

    text_xy = font.render('300', True, (255, 255, 255))  # White text
    text_rect = text_xy.get_rect(center=(300, 5))
    screen.blit(text_xy, text_rect)
    text_rect = text_xy.get_rect(center=(5, 300))
    screen.blit(text_xy, text_rect)

    # pygame.draw.aaline(screen, GREY, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
    # pygame.draw.aaline(screen, GREY, (0, SCREEN_HEIGHT / 2), (SCREEN_WIDTH, SCREEN_HEIGHT / 2))

    pygame.draw.ellipse(screen, RED, ball)
    pygame.draw.rect(screen, WHITE, thanh_truot)


    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()