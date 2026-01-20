#   Ham so
import  pygame
import  random
import may_bay_cau_hinh as cau_hinh

def tao_nhan_vat(hinh_anh, kich_thuoc, goc):
    nhan_vat = pygame.image.load(hinh_anh)
    nhan_vat = pygame.transform.scale(nhan_vat, (kich_thuoc["width"], kich_thuoc["height"]))
    nhan_vat = pygame.transform.rotate(nhan_vat, goc)

    nhan_vat_rect = nhan_vat.get_rect()

    return  {
        "nhan_vat": nhan_vat,
        "rect": nhan_vat_rect,
        "size": { "width": kich_thuoc["width"], "height": kich_thuoc["height"] },
        "speed": { "x": 0, "y": 0 },
        "ngang": random.randint(3, 7),
        "doc": random.randint(3, 7)
    }


def dieu_khien_may_bay(may_bay):
    may_bay["rect"].x = may_bay["rect"].x + may_bay["speed"]["x"]
    may_bay["rect"].y = may_bay["rect"].y + may_bay["speed"]["y"]

    may_bay["speed"]["x"] = 0
    may_bay["speed"]["y"] = 0

    #   ----------------Kiem tra vi tri ngang---------------
    if may_bay["rect"].x < 0:
        may_bay["rect"].x = 0

    if may_bay["rect"].x > cau_hinh.SCREEN_WIDTH - may_bay["size"]["width"]:
        may_bay["rect"].x = cau_hinh.SCREEN_WIDTH - may_bay["size"]["width"]

    #   ----------------Kiem tra vi tri doc---------------
    if may_bay["rect"].y < 0:
        may_bay["rect"].y = 0

    if may_bay["rect"].y > cau_hinh.SCREEN_HEIGHT - may_bay["size"]["height"]:
        may_bay["rect"].y = cau_hinh.SCREEN_HEIGHT - may_bay["size"]["height"]

def tao_ngoi_sao():
    return {
        "x": random.randint(-cau_hinh.SCREEN_WIDTH, cau_hinh.SCREEN_WIDTH),
        "y": random.randint(-cau_hinh.SCREEN_HEIGHT, cau_hinh.SCREEN_HEIGHT),
        "ban_kinh": random.randint(1, 2),
        "color": random.choice([cau_hinh.WHITE, cau_hinh.WHITE_1, cau_hinh.RED])
    }

def dieu_khien_ngoi_sao(ngoi_sao, toc_do):
    ngoi_sao["x"] = ngoi_sao["x"] + toc_do["ngang"]
    ngoi_sao["y"] = ngoi_sao["y"] + toc_do["doc"]

    if ngoi_sao["x"] < 0 or ngoi_sao["x"] > cau_hinh.SCREEN_WIDTH or ngoi_sao["y"] > cau_hinh.SCREEN_HEIGHT:
        ngoi_sao["x"] = random.randint(-cau_hinh.SCREEN_WIDTH, cau_hinh.SCREEN_WIDTH)
        ngoi_sao["y"] = random.randint(-cau_hinh.SCREEN_HEIGHT, cau_hinh.SCREEN_HEIGHT)

def tao_vien_dan():
    vien_dan = tao_nhan_vat("rocket-1.png", { "width": 32, "height": 32} , 0)
    vien_dan["toc_do"] = 20

    return  vien_dan

def dieu_khien_vien_dan(vien_dan):
    vien_dan["rect"].y = vien_dan["rect"].y - vien_dan["toc_do"]

    if vien_dan["rect"].y < 0:
        vien_dan["rect"].y = -100

def tao_ufo():
    hinh_anh = random.randint(1, 4)
    size = random.randint(12, 36)
    kich_thuoc = { "width": size, "height": size }

    ufo = tao_nhan_vat(str(hinh_anh) + ".png", kich_thuoc, 0)

    ufo["rect"].x = random.randint(0, cau_hinh.SCREEN_WIDTH)
    ufo["rect"].y = -100

    ufo["toc_do_y"] = random.randint(1, 5)
    ufo["toc_do_x"] = random.choice([-1, 1])

    ufo["status"] = 1
    ufo["danh_sach_vien_dan"] = []

    return ufo

def dieu_khien_ufo(ufo):
    if ufo["rect"].y < 100:
        ufo["rect"].y = ufo["rect"].y + ufo["toc_do_y"]
    else:
        ufo["rect"].x = ufo["rect"].x + ufo["toc_do_x"]

        if ufo["rect"].x < 0 or ufo["rect"].x > cau_hinh.SCREEN_WIDTH:
            ufo["toc_do_x"] = -ufo["toc_do_x"]

def kiem_tra_ufo(ufo, danh_sach_vien_dan):
    for vien_dan in danh_sach_vien_dan:
        if vien_dan["rect"].colliderect(ufo["rect"]):
            ufo["status"] = -1

            return

def tao_fire():
    hinh_anh = "fire.png"
    size = random.randint(12, 36)
    kich_thuoc = { "width": size, "height": size }

    fire = tao_nhan_vat(hinh_anh, kich_thuoc, 0)

    fire["status"] = 1

    return fire

def tao_ufo_vien_dan():
    vien_dan = tao_nhan_vat("rocket-fire.png", {"width": 24, "height": 24}, 0)
    vien_dan["toc_do"] = 5

    return vien_dan

def dieu_khien_ufo_vien_dan(vien_dan):
    vien_dan["rect"].y = vien_dan["rect"].y + vien_dan["toc_do"]

    if vien_dan["rect"].y > cau_hinh.SCREEN_HEIGHT:
        vien_dan["rect"].y = cau_hinh.SCREEN_HEIGHT + 100


def dieu_khien_ufo_ban_dan(ufo):
    kiem_tra = random.randint(1, 50)

    if kiem_tra == 50 and ufo["rect"].y > 0:
        vien_dan = tao_ufo_vien_dan()

        vien_dan["rect"].x = ufo["rect"].x + (ufo["size"]["width"] / 2)
        vien_dan["rect"].y = ufo["rect"].y + 10

        ufo["danh_sach_vien_dan"].append(vien_dan)

    danh_sach_ufo_vien_dan_nhap = []

    for vien_dan in ufo["danh_sach_vien_dan"]:
        dieu_khien_ufo_vien_dan(vien_dan)

        if vien_dan["rect"].y != cau_hinh.SCREEN_HEIGHT + 100:
            danh_sach_ufo_vien_dan_nhap.append(vien_dan)

    ufo["danh_sach_vien_dan"] = danh_sach_ufo_vien_dan_nhap

