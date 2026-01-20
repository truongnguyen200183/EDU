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

list_x = [i for i in list_so if ham_xu_ly.kiem_tra_so_nguyen_to(i) == True]
print(list_x)