#author: 王晓龙
#time: 2020/11/18 18:21
'''
    判断是否为会员？
    是会员：
        1.money>=200：打8折
        2.money >= 100 and money < 200：打9折
        3.其他：不打折
    不是会员：
        1.money >= 200：打95折
        2.其他：不打折
'''
fleg = input('你是否为会员?(y/n)')
money = float(input('请输入购买的金额：'))
if fleg == 'y':
    if money >= 200:
        print('打八折，需要支付的金额为：',money * 0.8)
    elif 100 <= money < 200:
        print('打九折，需要支付的金额为：',money * 0.9)
    else:
        print('不打折，需要支付的金额为：', money)
else:
    if money >= 200:
        print('打九五折，需要支付的金额为：',money * 0.95)
    else:
        print('不打折，需要支付的金额为：',money)