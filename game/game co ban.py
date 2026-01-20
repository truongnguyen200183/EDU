import  pygame

#   ----------------Thiet lap----------------
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game may bay")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (124, 114, 237)
GREY = (10, 10, 10)
BLUE = (0, 0, 255)

#   ----------------Bat dau----------------
running = True
clock = pygame.time.Clock()

while running == True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()