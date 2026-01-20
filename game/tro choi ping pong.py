import  pygame
import  random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game ping pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (124, 114, 237)
GREY = (10, 10, 10)
BLUE = (0, 0, 255)

thanh_truot = pygame.Rect(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT - 40, 100, 10)
qua_bong_original = pygame.image.load('ball.png')
qua_bong = pygame.transform.scale(qua_bong_original, (32, 32))
qua_bong_rect = qua_bong.get_rect()

qua_bong_rect.center = (SCREEN_WIDTH / 2 - 16, 50)

ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 * random.choice((1, -1))
moc_toc_do = 10

running = True
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
diem_so = 0

#   Khong dem gi ca
dem = { "thanh_truot": 0, "x": 0, "y": 0 }
#   dem = [0, 0, 0]

while running == True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    # if diem_so < 0:
    #     continue

    mouse_x = pygame.mouse.get_pos()[0]
    thanh_truot.centerx = mouse_x

    qua_bong_rect.x = qua_bong_rect.x + ball_speed_x
    qua_bong_rect.y = qua_bong_rect.y + ball_speed_y

    #   Dang dem so
    if dem["thanh_truot"] > 0:
        dem["thanh_truot"] = dem["thanh_truot"] + 1
    if dem["x"] > 0:
        dem["x"] = dem["x"] + 1
    if dem["y"] > 0:
        dem["y"] = dem["y"] + 1

    if qua_bong_rect.left <= 0 or qua_bong_rect.right >= SCREEN_WIDTH:
        if dem["x"] == 0:
            ball_speed_x = -ball_speed_x
            dem["x"] = 1

    if qua_bong_rect.top <= 0:
        if dem["y"] == 0:
            ball_speed_y = -ball_speed_y
            dem["y"] = 1

    if qua_bong_rect.bottom >= SCREEN_HEIGHT:
        if dem["y"] == 0:
            ball_speed_y = -ball_speed_y
            diem_so = diem_so - 1

            dem["y"] = 1

    if qua_bong_rect.colliderect(thanh_truot):
        if dem["thanh_truot"] == 0:
            ball_speed_y = -ball_speed_y

            if(qua_bong_rect.y < thanh_truot.y):
                diem_so = diem_so + 1

            dem["thanh_truot"] = 1

    if dem["thanh_truot"] > 10:
        dem["thanh_truot"] = 0
    if dem["x"] > 10:
        dem["x"] = 0
    if dem["y"] > 10:
        dem["y"] = 0

    if diem_so >= moc_toc_do:
        moc_toc_do = moc_toc_do + 10

        ball_speed_x = ball_speed_x * 1.5
        ball_speed_y = ball_speed_y * 1.5

    text_diem_so = font.render("Score: " + str(diem_so), True, BLUE)

    #   ----------------Hien thi----------------

    screen.fill(WHITE)

    #pygame.draw.ellipse(screen, RED, qua_bong)
    screen.blit(qua_bong, qua_bong_rect)

    pygame.draw.rect(screen, PURPLE, thanh_truot)
    screen.blit(text_diem_so, (20, 20))

    if diem_so < 0:
        text_stop = font.render("Ban da thua cuoc", True, RED)
        screen.blit(text_stop, (SCREEN_WIDTH / 2 - text_stop.get_width() / 2, SCREEN_HEIGHT / 2 - 50))

    #pygame.draw.aaline(screen, GREY, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()