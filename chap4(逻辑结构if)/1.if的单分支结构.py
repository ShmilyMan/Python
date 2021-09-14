#author: 王晓龙
#time: 2020/11/18 17:37
money = 1000
s = int(input('请输入取款金额'))
if s <= money:
    money = money - s;
    print("余额为：",money)
