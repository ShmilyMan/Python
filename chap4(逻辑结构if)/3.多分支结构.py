#author: 王晓龙
#time: 2020/11/18 17:53
'''
    从键盘输入一个成绩，并判断成绩所属的范围
    0~59：F
    60~69：D
    70~79：C
    80~89：B
    90~100：A
'''
score = int(input('请输入一个学生的成绩：'))
if 0 <= score <= 59:
    print('F')
elif 60 <= score <= 69:
    print('D')
elif 70 <= score <= 79:
    print('C')
elif 80 <= score <= 89:
    print('B')
elif 90 <= score <= 100:
    print('A')
else:
    print('成绩输入非法，不在成绩的有效范围')