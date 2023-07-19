"""
1、编写程序，使用循环语句输出1+2+3+…+100的和。
"""
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

"""
2、编写程序，使用循环语句输出1+4+7+10+13+…+112的和。
"""
# sum = 0
# for i in range(1,113,3):
#     sum += i
# print(sum)


"""
3．编程程序，使用循环语句输出5+10+15+20+25+…+100的和
"""
# sum = 0
# for i in range(5,101,5):
#     sum += i
# print(sum)

"""
4. 编写程序，输入一个18位的身份证号码，从中提取出生日期，并以“出生日期是*年*月*日”样的格式输出。
500384199705045827               字符串的切片
"""
# ID = input("请输入您的身份证号：")
# year = ID[6:10]
# month = ID[10:12]
# date = ID[12:14]
# print(year,month,date)
# print("出生日期是{}年{}月{}日".format(year,month,date))

"""
5. 编写函数IsPrime(n)，用来判断整数n是否为素数，并编写测试代码,调用该函数。
"""

def IsPrime(n):

    a = int(n/2 + 1)

    for i in range(2,a):
        if n % i == 0:
            print("不是素数")
        else:
            print("是素数")
IsPrime(3)








