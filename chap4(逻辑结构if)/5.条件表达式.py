#author: 王晓龙
#time: 2020/11/18 18:41
'''简化else...if的操作'''
'''
    输入两个数，并判断他们的大小
'''
num1 = int(input('请输入第一个整数'))
num2 = int(input('请输入第二个整数'))
# if条件如果成立，则执行前面的语句，如果不成立，则执行else后面的语句
print(str(num1) + '>=' + str(num2) if num1 >= num2 else str(num1) + '<' + str(num2))