#author: 王晓龙
#time: 2020/11/17 10:19
n1 = 1.1
n2 = 2.2
print(n1 + n2) #使用浮点数时，可能出现计算不精确的情况（float类型）

#解决方法：导入Decimal模块
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))
