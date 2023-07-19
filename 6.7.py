"""
1、如何判断一个数组是对称数组？
"""
# def test():
#     a = [1,2,3,4,5]
#     b = [5,4,3,2,1,1]
#     if b == a[::-1]:
#         return True
#     else:
#         return False
#
# print(test())

"""
2. 对列表 a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8] 中的数字从小到大排序。
"""
# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
# print(sorted(a,reverse=False))  # 用sorted()函数 对可迭代对象 进行排序； 从小到大排序
# # [1, 1, 6, 6, 7, 8, 8, 8, 8, 9, 11]
#
# b = (1,2,3,4,5)
# print(sorted(b,reverse=True))  # 从大到小排列，元组排序后是一个列表
# # [5, 4, 3, 2, 1]
#
# c = ('a','T','y','r','E')
# print(sorted(c))  # 按从ASCII码 默认从小到大排序，元组排序后是一个列表
# # ['E', 'T', 'a', 'r', 'y']
#
#
# str = "fdfaad"
# print(sorted(str))  # 排序之后是一个列表
# # ['a', 'a', 'd', 'd', 'f', 'f']



"""
3、找出列表 L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88] 中最大值和最小值。
"""
# L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
# print(max(L1))
# print(min(L1))



"""
4. 找出列表 a = [“hello”, “world”, “yoyo”, “congratulations”] 中单词最长的一个。
"""
# a = ["hello", "world", "yoyo", "congratulations"]
#
# length = len(a[0])   # 比较题目，可以先定一个标准；其他数都与这个比较
#
# for i in range(0,len(a)):
#     if len(a[i]) > length:
#         print(a[i])


"""
5. 取出列表 L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88] 中最大的三个值。
"""
# 思路：将这个列表从大到小排序后，取前三个数
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
print(sorted(L1,reverse=True)[0:3])





