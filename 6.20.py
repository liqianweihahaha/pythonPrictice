"""
1、幂的计算；比如怎么计算2的三次方
"""
# print(2**3)    # 利用运算符
# print(pow(2,3))   # 直接通过pow函数

"""
2、如何将字符列表 转换为字符串----用join连接
"""
# l = ['Python','Circle','is','ok']
# print(' '.join(l))   # Python Circle is ok

"""
3、怎么快速打印出包含所有ASCII字母（大写和小写）的字符串
"""
import string
print(string.ascii_lowercase)  # 利用string模块，可以输出所有的小写字母
print(string.ascii_uppercase)  # 输出所有的大写字母
print(string.ascii_letters)   # 输出所有的字母（包括小写和大写）
print(string.digits)   # 0123456789  输入所有的数字

"""
4、怎么让字符串居中？
"""
str = '小鱼python'
print(str.center(50))   #center()方法，可以在字符串左右 自动填充字符（默认是填充空格），也可以指定填充字符
print(str.center(50,'*'))   # 指定填充字符


"""
5、怎么在字符串中找到子串？
"""
# ss = 'I love python'
# print(ss.find('o'))   # 用find方法，能找到就会返回索引，找不到就会返回-1















