#author: 王晓龙
#time: 2020/11/18 17:50
'''从键盘输入一个整数，并判断它是奇数还是偶数'''
num = int(input('请输入一个整数：'))
if num % 2 == 0:
    print(num,'为偶数')
else:
    print(num,'为奇数')