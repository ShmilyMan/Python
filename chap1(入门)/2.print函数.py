#author: 王晓龙
#time: 2020/11/16 21:56
#1.输出数字
print(520)

#2.输出字符串
print("hallow world")

#3.输出含有运算符的表达式
print(44+55)

#4.输出到文件中
fp = open("D:/test.txt", "a+")#当文件不存在时则创建，如果文件存在，则在文件末尾追加所要追加的内容
print("hallow world",file=fp)
fp.close()#关闭打开的文件

#5.进行不换行的输出
print("hallow","world","python")

