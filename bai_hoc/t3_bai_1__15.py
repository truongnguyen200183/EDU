import  ham_xu_ly
list_so = [10, 25, 30, 45, 50, 30, 25, 3, 7, 9, 11]
x = 30

# vi_tri = -1
# for i in range(len(a)):
#     if x == a[i]:
#         if vi_tri == -1:
#             vi_tri = i
#
# print(vi_tri)

# dem = 0
# for i in list_so:
#     if i > x:
#         dem += 1
#         print(i)
#
# print(dem)

# list_k = [i for i in list_so if i > x]
# print(list_k)

# list_so_chan = []
# list_so_le = []
#
# for i in list_so:
#     if i % 2 == 0:
#         list_so_chan.append(i)
#     else:
#         list_so_le.append(i)

# list_so_chan = [i for i in list_so if i % 2 == 0]
# list_so_le = [i for i in list_so if i % 2 == 1]
#
# print(list_so_chan)
# print(list_so_le)

# dem = 0
# for i in list_so:
#     kiem_tra = ham_xu_ly.kiem_tra_so_nguyen_to(i)
#
#     if kiem_tra == True:
#         dem += 1
#
# print(dem)

# list_x = [i for i in list_so if ham_xu_ly.kiem_tra_so_nguyen_to(i) == True]
# print(list_x)

mang = [1, 3, 2, 4, 15, 1, 2, 6, 5, 5, 5]

# mang_moi = []
#
# for i in mang:
#     if mang_moi.count(i) == 0:
#         mang_moi.append(i)
#
# mang = mang_moi
#
# vi_tri = 0
# while vi_tri < len(mang):
#     gia_tri_kiem_tra = mang[vi_tri]
#
#     if mang.count(gia_tri_kiem_tra) > 1:
#         mang_moi.remove(gia_tri_kiem_tra)
#     else:
#         vi_tri += 1
#
# print(mang)

#   7
#   Sap xep Bubble Sort

so_luong = len(mang)

# for i in range(so_luong - 1):
#     a = mang[i]
#     for j in range(i + 1, so_luong):
#         b = mang[j]
#
#         if a > b:
#             mang[i] = b
#             mang[j] = a

# for i in range(so_luong - 1):
#     for j in range(i + 1, so_luong):
#         if mang[i] > mang[j]:
#             temp = mang[i]
#             mang[i] = mang[j]
#             mang[j] = temp

# print(mang)

#   12
# max1 = mang[0]      #   lon nhat
# max2 = mang[1]      #   lon nhi
#
# if max1 < max2:
#     max1 = mang[1]
#     max2 = mang[0]
#
# for i in range(2, so_luong):
#     if mang[i] > max2:
#         max2 = mang[i]
#
#         if max1 < max2:
#             temp = max1
#             max1 = max2
#             max2 = temp
#
# print(max1)
# print(max2)

#   13
mang_so = []
mang_dem = []

for i in mang:
    if mang_so.count(i) == 0:
        mang_so.append(i)

        so_lan = mang.count(i)
        mang_dem.append(so_lan)

print(mang_so)
print(mang_dem)