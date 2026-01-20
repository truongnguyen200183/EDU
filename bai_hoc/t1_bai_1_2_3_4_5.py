import  math
import  ham_xu_ly as my_math

#1
a  = int(input())
tong = 0

#   C1:

# day_chu_so_a = str(a)
#
# for chu_so in day_chu_so_a:
#     gia_tri = int(chu_so)
#
#     tong = tong + gia_tri


#   C2:

while a > 0:
    hang_don_vi = a % 10
    tong = tong + hang_don_vi

    a = a - hang_don_vi
    a = int(a / 10)

print(tong)

#2
# a = int(input())
# b = int(input())
# c = int(input())

# so_lon_nhat = a
# so_nho_nhat = a
#
# if a < b:
#     so_lon_nhat = b
# else:
#     so_nho_nhat = b
#
# if so_lon_nhat < c:
#     so_lon_nhat = c
# else:
#     if so_nho_nhat > c:
#         so_nho_nhat = c

print("Nhap vao cac so tu nhien, nhap ky tu khac so de ket thuc")

danh_sach = []
key = input()
while key.isnumeric():
    so = int(key)
    danh_sach.append(so)

    key = input()

so_lon_nhat = danh_sach[0]
so_nho_nhat = danh_sach[0]

for i in range(1, len(danh_sach)):
    if so_lon_nhat < danh_sach[i]:
        so_lon_nhat = danh_sach[i]
    if so_nho_nhat > danh_sach[i]:
        so_nho_nhat = danh_sach[i]

print(so_lon_nhat)
print(so_nho_nhat)

#3
r = int(input())

chu_vi =  2 * r * math.pi
dien_tich = r * r * math.pi

lam_tron = input()
lam_tron = "." + lam_tron + "f"

chu_vi = format(chu_vi, lam_tron)
dien_tich = format(dien_tich, lam_tron)

print(chu_vi)
print(dien_tich)

#4
a = 10
b = 20
c = 5
d = 100

ucln_ab = my_math.uoc_dung_lon_nhat(a, b)
ucln_abc =  my_math.uoc_dung_lon_nhat(ucln_ab, c)
ucln_abcd =  my_math.uoc_dung_lon_nhat(ucln_abc, d)

ucln_tt = a
ucln_tt =  my_math.uoc_dung_lon_nhat(ucln_tt, a)
ucln_tt =  my_math.uoc_dung_lon_nhat(ucln_tt, b)
ucln_tt =  my_math.uoc_dung_lon_nhat(ucln_tt, c)
ucln_tt =  my_math.uoc_dung_lon_nhat(ucln_tt, d)

print(ucln_abc)

#5
bcnn_ab =  my_math.boi_chung_nho_nhat(a, b)

print(bcnn_ab)

#4.1
#   3 5 2 5 6 7 42
#   ["3", "5", "2", "5", "6", "7", "42"]
#   [3, 5, 2, 5, 6, 7, 42]

list_so = list(map(int, input().split()))

ucln_tt = list_so[0]

for i in range(1, len(list_so)):
    so_thu_hai = list_so[i]

    ucln_tt =  my_math.uoc_dung_lon_nhat(ucln_tt, so_thu_hai)

print(ucln_tt)

ucln_tt = list_so[0]
for b in list_so:
    ucln_tt =  my_math.uoc_dung_lon_nhat(ucln_tt, b)

