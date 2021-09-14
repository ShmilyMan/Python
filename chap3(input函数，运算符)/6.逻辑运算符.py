#author: 王晓龙
#time: 2020/11/18 11:07
a = 10
b = 10
print("---------and 与-----------")
print(a == 10 and b == 10)
print(a != 10 and b == 10)
print(a == 10 and b != 10)
print(a != 10 and b != 10)
print("---------or 或-----------------")
print(a == 10 or b == 10)
print(a != 10 or b == 10)
print(a == 10 or b != 10)
print(a != 10 or b != 10)
print("-------------not 非------------------")
fleg1 = True
fleg2 = False
print(not fleg1)
print(not fleg2)
print("-----------in 包含 not in 不包含-------------------")
str1 = 'halllewworld'
str2 = 'a'
print(str2 in str1)
print(str2 not in str1)