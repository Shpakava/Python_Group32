"""
Напишите программу, которая на вход получает строку чисел, а на выход выдает последовательность 1 и 0.
При этом, если число в строке больше 4, то его заменить на 1, в обратном случае на 0

5124956332
"""
num = input()
res = ""
# for i in num:
#     if int(i) > 4:
#         res += "1"
#     else:
#         res += "0"
# print(res)


for i in range(len(num)):
    if int(num[i]) > 4:
        res += "1"
    else:
        res += "0"
print(res)
