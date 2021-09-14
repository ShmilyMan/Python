#author: 王晓龙
#time: 2020/11/16 22:17
print('hallow\nworld')  #换行
print('hallow\tworld')  #水平制表符
print('hallow\bworld')  #退格，它向前退一个字符的位置
print('hallow\rworld')  #回车，字符的位置将退回到起始编辑的位置

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')
print("aaa"+"sss")  # + 在字符串的后边不能追加数字

#原字符：使转义字符失去作用的字符，就是在字符串的前面加上r或者R
print(r'hallow\nworld') #此时，转义字符被当做普通的字符串进行处理