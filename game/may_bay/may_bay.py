import  pygame
import  random

import may_bay_cau_hinh as cau_hinh
import may_bay_xu_ly as xu_ly

#   ----------------Thiet lap----------------
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((cau_hinh.SCREEN_WIDTH, cau_hinh.SCREEN_HEIGHT))
pygame.display.set_caption(cau_hinh.TITLE)

boom_sound = pygame.mixer.Sound("boom.mp3")
bg_sound = pygame.mixer.Sound("bg.wav")
font = pygame.font.Font(None, 36)

#   ----------------May bay----------------

mau = 100
may_bay = xu_ly.tao_nhan_vat("may_bay.png", { "width":64, "height": 64 }, 45 )
may_bay["rect"].center = (cau_hinh.SCREEN_WIDTH / 2, cau_hinh.SCREEN_HEIGHT - 100)

#   ----------------Ngoi sao----------------
toc_do = {
    "ngang": random.randint(-1, 1),
    "doc": random.randint(1, 3)
}

#   ----------------UFO----------------
do_kho = 40
dem_toc_do = 0

danh_sach_ngoi_sao = []

so_ngoi_sao = 100
for i in range(so_ngoi_sao):
    ngoi_sao = xu_ly.tao_ngoi_sao()
    danh_sach_ngoi_sao.append(ngoi_sao)

#   ----------------Vien dan----------------

dem_ban = 0
danh_sach_vien_dan = []

#   ----------------UFO----------------

dem_tao_ufo = 0
danh_sach_ufo = []

#   ----------------Fire----------------
danh_sach_fire = []

#   ----------------Bat dau----------------
running = True
clock = pygame.time.Clock()

go_loi = 0
bg_sound.play(loops = -1)

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #   ----------------Dieu khien may bay---------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        may_bay["speed"]["x"] = -may_bay["ngang"]
    elif keys[pygame.K_RIGHT]:
        may_bay["speed"]["x"] = may_bay["ngang"]

    if keys[pygame.K_UP]:
        may_bay["speed"]["y"] = -may_bay["doc"]
    elif keys[pygame.K_DOWN]:
        may_bay["speed"]["y"] = may_bay["doc"]

    xu_ly.dieu_khien_may_bay(may_bay)

    if dem_toc_do > 1000:
        toc_do = {
            "ngang": random.randint(-1, 1),
            "doc": random.randint(1, 3)
        }

        dem_toc_do = 0
    else:
        dem_toc_do = dem_toc_do + 1

    if keys[pygame.K_SPACE]:
        if dem_ban == 0:
            vien_dan = xu_ly.tao_vien_dan()

            vien_dan["rect"].x = may_bay["rect"].x + (may_bay["size"]["width"] / 2)
            vien_dan["rect"].y = may_bay["rect"].y

            danh_sach_vien_dan.append(vien_dan)

        dem_ban = dem_ban + 1

        if dem_ban == 2:
            dem_ban = 0

    #   ----------------Ve nen----------------
    screen.fill(cau_hinh.BLACK)


    #   ----------------Ve ngoi sao----------------
    for ngoi_sao in danh_sach_ngoi_sao:
        xu_ly.dieu_khien_ngoi_sao(ngoi_sao, toc_do)

        pygame.draw.circle(screen, ngoi_sao["color"], (ngoi_sao["x"], ngoi_sao["y"]), ngoi_sao["ban_kinh"], 0)


    #   ----------------Ve vien dan----------------
    danh_sach_vien_dan_nhap = []

    for vien_dan in danh_sach_vien_dan:
        xu_ly.dieu_khien_vien_dan(vien_dan)

        if vien_dan["rect"].y != -100:
            danh_sach_vien_dan_nhap.append(vien_dan)

        screen.blit(vien_dan["nhan_vat"], vien_dan ["rect"])

    danh_sach_vien_dan = danh_sach_vien_dan_nhap


    #   ----------------Ve UFO----------------

    if dem_tao_ufo > do_kho:
        ufo_moi = xu_ly.tao_ufo()
        danh_sach_ufo.append(ufo_moi)

        dem_tao_ufo = 0
    else:
        dem_tao_ufo = dem_tao_ufo + 1

    danh_sach_ufo_nhap = []
    for ufo in danh_sach_ufo:
        xu_ly.dieu_khien_ufo(ufo)

        xu_ly.kiem_tra_ufo(ufo, danh_sach_vien_dan)

        if ufo["status"] == 1:
            screen.blit(ufo["nhan_vat"], ufo["rect"])

            danh_sach_ufo_nhap.append(ufo)

            #   ----------------UFO ban dan----------------
            xu_ly.dieu_khien_ufo_ban_dan(ufo)

            danh_sach_vien_dan_nhap = []
            for ufo_vien_dan in ufo["danh_sach_vien_dan"]:
                if ufo_vien_dan["rect"].colliderect(may_bay["rect"]):
                    mau = mau - 1

                    fire = xu_ly.tao_fire("fire2.png")
                    fire["rect"].x = ufo_vien_dan["rect"].x
                    fire["rect"].y = ufo_vien_dan["rect"].y

                    danh_sach_fire.append(fire)
                    boom_sound.play()
                else:
                    danh_sach_vien_dan_nhap.append(ufo_vien_dan)
                    screen.blit(ufo_vien_dan["nhan_vat"], ufo_vien_dan["rect"])

            ufo["danh_sach_vien_dan"] = danh_sach_vien_dan_nhap
        else:
            fire = xu_ly.tao_fire()
            fire["rect"].x = ufo["rect"].x
            fire["rect"].y = ufo["rect"].y

            danh_sach_fire.append(fire)

            boom_sound.play()

    danh_sach_ufo = danh_sach_ufo_nhap

    #   ----------------Ve Fire----------------

    danh_sach_fire_nhap = []

    for fire in danh_sach_fire:
        if fire["status"] < 3:
            screen.blit(fire["nhan_vat"], fire["rect"])

            fire["status"] = fire["status"] + 1

            danh_sach_fire_nhap.append(fire)

    danh_sach_fire = danh_sach_fire_nhap

    #   ----------------Ve may bay----------------
    screen.blit(may_bay["nhan_vat"], may_bay["rect"])

    text_mau = font.render("Mau: " + str(int(mau)), True, cau_hinh.WHITE)
    screen.blit(text_mau, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()