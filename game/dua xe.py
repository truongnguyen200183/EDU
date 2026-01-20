import  pygame
import  random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game dua xe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (124, 114, 237)
GREY = (100, 100, 100)

font = pygame.font.Font(None, 36)

con_duong = pygame.Rect(0, 0, SCREEN_WIDTH - 400, SCREEN_HEIGHT)
con_duong.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

min_y = -25
max_y = 625
goc_center_y = min_y

#   ----------------Xe----------------
toc_do = 0
car_size = { "width": 96, "height": 96 }
car_original = pygame.image.load('car1.png')
car = pygame.transform.scale(car_original, (car_size["width"], car_size["height"]))

car_rect = car.get_rect()
car_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)

car_speed = { "x": 0, "y": 0 }

#   ----------------Xe doi thu----------------
car_original_doi_thu = pygame.image.load('car.png')
car_doi_thu = pygame.transform.scale(car_original_doi_thu, (car_size["width"], car_size["height"]))

#car_doi_thu = pygame.transform.rotate(car_doi_thu, 90)

car_rect_doi_thu = car_doi_thu.get_rect()
car_rect_doi_thu.center = (random.randint(200, 600), -100)
toc_do_doi_thu = random.randint(85, 95)

#   ----------------Tree----------------
tree1 = pygame.image.load('tree.png')
tree_rect_1 = tree1.get_rect()
tree_rect_1.center = (random.randint(0, 180), random.randint(-1000, -100))

tree2 = pygame.image.load('tree.png')
tree_rect_2 = tree2.get_rect()
tree_rect_2.center = (random.randint(600, 780), random.randint(-1000, -100))

#   ----------------Bat dau----------------
running = True
clock = pygame.time.Clock()

while running == True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_speed["x"] = -5
    elif keys[pygame.K_RIGHT]:
        car_speed["x"] = 5

    car_rect.x = car_rect.x + car_speed["x"]
    car_speed["x"] = 0

    if car_rect.x < 0:
        car_rect.x = 0

    if car_rect.x > SCREEN_WIDTH - car_size["width"]:
        car_rect.x = SCREEN_WIDTH - car_size["width"]

    if keys[pygame.K_UP] == True:
        toc_do = toc_do + 0.1
    elif keys[pygame.K_DOWN] == True:
        toc_do = toc_do - 2
    else:
        toc_do = toc_do - 0.01

    if car_rect.x < 200 or car_rect.x > 550:
        toc_do = toc_do - 3

    if toc_do < 0:
        toc_do = 0
    elif toc_do > 100:
        toc_do = 100

    text_toc_do = font.render("Speed: " + str(int(toc_do)), True, BLUE)

    hieu_toc_do = toc_do_doi_thu- toc_do
    car_rect_doi_thu.y = car_rect_doi_thu.y - hieu_toc_do

    if(car_rect_doi_thu.y < -100):
        car_rect_doi_thu.y = -100

    #   ----------------Kiem tra vuot xe----------------
    if car_rect_doi_thu.y > SCREEN_HEIGHT + 100:
        car_rect_doi_thu.center = (random.randint(200, 600), -100)
        toc_do_doi_thu = random.randint(85, 95)

    #   ----------------Hien thi----------------

    screen.fill(GREEN)
    #pygame.draw.aaline(screen, GREY, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    pygame.draw.rect(screen, GREY, con_duong)

    #   ----------------Hien thi cay----------------
    tree_rect_1.y = tree_rect_1.y + toc_do
    tree_rect_2.y = tree_rect_2.y + toc_do

    if tree_rect_1.y > SCREEN_HEIGHT + 200:
        tree_rect_1.center = (random.randint(0, 180), random.randint(-1000, -100))
    if tree_rect_2.y > SCREEN_HEIGHT + 200:
        tree_rect_2.center = (random.randint(600, 780), random.randint(-1000, -100))

    screen.blit(tree1, tree_rect_1)
    screen.blit(tree2, tree_rect_2)

    #   ----------------Hien thi vach ke duong----------------

    goc_center_y = goc_center_y + toc_do
    if goc_center_y > max_y:
        goc_center_y = min_y

    #   ----------------Hien thi vach ke duong chieu di xuong----------------
    vach_ke_center_y = goc_center_y

    while vach_ke_center_y < max_y:
        vach_ke = pygame.Rect(0, 0, 10, 50)

        vach_ke.center = (SCREEN_WIDTH / 2, vach_ke_center_y)
        pygame.draw.rect(screen, WHITE, vach_ke)

        vach_ke_center_y = vach_ke_center_y + 70

    #   ----------------Hien thi vach ke duong chieu di len----------------
    vach_ke_center_y = goc_center_y

    while vach_ke_center_y > min_y:
        vach_ke = pygame.Rect(0, 0, 10, 50)

        vach_ke.center = (SCREEN_WIDTH / 2, vach_ke_center_y)
        pygame.draw.rect(screen, WHITE, vach_ke)

        vach_ke_center_y = vach_ke_center_y - 70

    #   ----------------Hien thi xe chinh----------------
    screen.blit(car, car_rect)
    screen.blit(text_toc_do, (20, 20))

    #   ----------------Hien thi xe phu----------------
    screen.blit(car_doi_thu, car_rect_doi_thu)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()