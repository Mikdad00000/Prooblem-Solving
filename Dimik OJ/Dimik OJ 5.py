# koita = int(input())
# i = 0
# while koita > i:
#     x = int(input())
#     j = 0
#     while j < x:
#         k = 0
#         while k < x:
#             print("*", end="")
#             k = k + 1
#         print("")
#         j = j + 1
#     print("")
#     i = i + 1
#
# input
# 2
# 3
# 4
#
# output
# *
# **
# ***
#
# *
# **
# ***
# ****

koita = int(input())
A = 0
while koita > A:
    tinput = int(input())
    B = 0
    while B < tinput:
        print("*")
        B = B + 1
    print("")
    A = A + 1

# input
# 2
# 3
# 4

# output
# ***
# **
# *

# ****
# ***
# **
# *



# input
# 2
# 3
# 4
#
# output
#   *
#  **
# ***
