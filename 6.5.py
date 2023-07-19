"""
9. 已知一个字符串为 “hello_world_yoyo”，如何得到一个队列 [“hello”,”world”,”yoyo”] ？
"""
# test = "hello_world_yoyo"
# test1 = test.split("_")  # 按字符串分割
# print(test1)
# test2 = test.split("_",1)   # 可以指定分割的次数
# print(test2)
# test3 = test.split()  # 不带参数，默认按空白字符分割
# print(test3)

"""
10. 有个列表 [“hello”, “world”, “yoyo”]，如何把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”？
"""
# list = ["hello", "world", "yoyo"]
# str1 = "_".join(list)
# print(str1)


"""
11. 把字符串 s 中的每个空格替换成”%20”，输入：s = “We are happy.”，输出：“We%20are%20happy.”。
"""
# s = "We are happy."
# print(s.replace(" ","%20"))


"""
12. Python 如何打印 99 乘法表？
"""
# for i in range(1,10):  # i代表行
#     for j in range(1,i+1):  # j代表列
#         print("{}x{}={}\t".format(j,i,i*j),end="")
#     print()   # 每次内循环结束后，输出一个空行


"""
13. 从下标 0 开始索引，找出单词 “welcome” 在字符串“Hello, welcome to my world.” 中出现的位置，找不到返回 -1。
"""
# def findStr():
#     message = "Hello, welcome to my world."
#     word = "welcome"
#     if word in message:
#         return message.find(word)
#     else:
#         return -1
#
# print(findStr())










