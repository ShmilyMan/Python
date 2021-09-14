#author: 王晓龙
#time: 2020/11/18 10:13
a = 10;
b = 10;
list1 = [11,22,33,44]
list2 = [11,22,33,44]
# -----------比较值--------------
# == 号用于比较两个变量的值
print(a > b) # False
print(a < b) # False
print(a >= b) # Ture
print(a <= b) # Ture
print(a == b) # Ture
print(a != b) # False
# ------------比较内存的标识符的地址-------------------
# is,is not 用于比较两个变量在内存中的地址是否相同
print(a is b) # Ture
print(a is not b) # False

print(list1 == list2) # Ture
print(list2 is list1) # False --> 两个变量存放在不同的内容地址中
