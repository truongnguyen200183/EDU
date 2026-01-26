
import  ham_xu_ly

mang = [1, 3, 2, 4, 15, 1, 2, 6, 5, 5, 5]

mang_moi = []

for i in mang:
    if mang_moi.count(i) == 0:
        mang_moi.append(i)

mang = mang_moi

vi_tri = 0
while vi_tri < len(mang):
    gia_tri_kiem_tra = mang[vi_tri]

    if mang.count(gia_tri_kiem_tra) > 1:
        mang_moi.remove(gia_tri_kiem_tra)
    else:
        vi_tri += 1

print(mang)
