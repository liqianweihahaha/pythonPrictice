"""
14. 统计字符串“Hello, welcome to my world.” 中字母 w 出现的次数。
"""
# message = "Hello, welcome to my world."
# count = message.count("w",0,8)
# print(count)


"""
15. 判断字符串 a = “welcome to my world” 是否包含单词 b = “world”，包含返回 True，不包含返回 False。
"""
# def findStr():
#
#     a = "welcome to my world"
#     b = "world"
#     if b in a:
#         return True
#     else:
#         return False
#
# print(findStr())


"""
16、从 0 开始计数，输出指定字符串 A = “hello” 在字符串 B = “hi how are you hello world, hello yoyo!”中第一次出现的位置，
如果 B 中不包含 A，则输出 -1
"""
# def findIndex():
#     A = "hello"
#     B = "hi how are you hello world, hello yoyo!"
#
#     if A in B:
#         return B.find(A)
#     else:
#         return -1
#
#
# print(findIndex())


"""
17. 将字符串 s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”。
"""
# 去重方法一
# s = "ajldjlajfdljfddd"
# s = set(s)
# print(s)
#
# s = list(s)
# print(s)
#
# s.sort(reverse=False)
# s = "".join(s)
# print(s)

# 去重方法二
# s = "ajldjlajfdljfddd"
# newStr = ""
# for char in s:
#     if char not in newStr:
#         newStr += char
#
# newStrList = list(newStr)  # 将字符串转为列表
# newStrList.sort(reverse=False)   # 将列表中的元素进行排序，sort
# result = "".join(newStrList)  # 将列表中的元素 用join连接起来，转为字符串
# print(result)


# """
# 18、求 1+2+3…+100 相加的和。
# """
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)



"""
19. 已知 a 的值为“hello”，b 的值为“world”，如何交换 a 和 b 的值，得到 a 的值为“world”，b 的值为”hello”？
"""
a = 'hello'
b = 'world'

c = a
a = b
b = c

print(a,b)
