"""
1、编写一个程序，查找所有此类数字，它们可以被7整除，但不能是5的倍数（在2000和3200之间（均包括在内））。
 获得的数字应以逗号分隔的顺序打印在一行上。
"""
# l = []
# for i in range(2000,3200):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
#
# str = ','.join(l)    # join连接列表、元组前，需要把其中的元素 转为字符串
# print(str)


"""
2、编写一个程序，可以计算给定数字的阶乘，结果应以逗号分隔的顺序打印在一行上，假设向程序提供了以下输入：8然后，输出应为：40320
"""
# i = int(input('请输入一个数字: '))
# fact = 1
# for i in range(1,i+1):
#     fact = fact * i
#
# print(fact)


"""
3、使用给定的整数n，编写程序以生成包含（i，ixi）的字典，该字典为1到n之间的整数（都包括在内）。然后程序应打印字典
假设向程序提供了以下输入：8
然后，输出应为：
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
# i = int(input("请输入一个数字："))
# dict1 = {}
# for i in range(1,i+1):
#     dict1[i] = i * i
#
# print(dict1)



"""
4、求前n阶乘的和：比如求1 + 2！ + 3！ + .... + 10!的和。
"""
# i = int(input("请输入一个数字："))
# fact = 1
# sum = 0
# for i in range(1,i+1):
#     fact = fact * i
#     sum = sum + fact
# print("前{}个数的阶乘是：{}".format(i,sum))


"""
5、求两个列表中的相同元素和不同元素
list1 = [1,2,3]
list2 = [3,4,5]

输出：
list1 和 list2 的相同元素是：[3]
list1 和 list2 的不同元素是: [1,2,4,5]
"""
# list1 = [1,2,3]
# list2 = [3,4,5]
#
# set1 = set(list1)
# set2 = set(list2)
#
# print("list1和list2的相同元素（交集）是：",set1 & set2)
# print("list1和list2的相同（差集）元素是：",set1 ^ set2)
# print("list1和list2的并集是：",set1 | set2)




"""
6、列表转换成字典
输入：
m = ['a',11]
n = ['b',22]
输出：
{'a':11,'b':22}
"""
# m = ['a',11]
# n = ['b',22]
# print(dict([m]))
# print(dict([n]))
# print(dict([m,n]))


"""
7、倒序输出列表中的数据
输入：a = ['one','two','three']
输出:
three
two
one
"""
# a = ['one','two','three']
# a1 = a[::-1]
# for i in a1:
#     print(i)


"""
8、100以内的偶数和
用for循环实现1-100之间的偶数之和
"""
# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum += i
# print(sum)













