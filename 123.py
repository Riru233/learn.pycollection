# print("hello world!")

#第一次作业 输入一个字符串，占20位，用加号填充，并输出
# from re import X


# a=input()
# print("{:+<20}".format(a))

#第二次作业 列表相乘
# x1=[2,6,3]
# x2=eval(input("请输入"))
# x3=0
# for i in range(len(x1)):
#     x3+=x1[i]*x2[i]
# print(x3)

#第三次作业 随机序列
import random
random.seed(123)
for i in range(11):
    print(random.randint(1,999),end=',')