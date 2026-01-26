def uoc_dung_lon_nhat(a, b):
    so_du = a
    while so_du > 0:
        so_du = a % b
        a = b
        b = so_du

    return a

def boi_chung_nho_nhat(a, b):
    ucln = uoc_dung_lon_nhat(a, b)

    return a * b / ucln

def tim_so_uoc(x):
    so_uoc_x = 0

    for j in range(2, x // 2 + 1):
        if x % j == 0:
            so_uoc_x += 1

    return so_uoc_x + 2

def kiem_tra_so_nguyen_to(x):
    so_uoc = tim_so_uoc(x)

    if so_uoc == 2:
        return True
    else:
        return False

def kiem_tra_so_chinh_phuong(x):
    a = int(x ** 0.5)

    if x == a * a:
        return True
    else:
        return False