"""
1、把列表 a = [1, -6, 2, -5, 9, 4, 20, -3] 中的数字绝对值。
"""
# a = [1, -6, 2, -5, 9, 4, 20, -3]
#
# list = []
# for i in range(0,len(a)):
#     list.append(abs(a[i]))
#
# print(list)

"""
2、寻找字符串中唯一的元素------------set集合的相关操作
str = "wwwweeeegtwrewee"
"""
# str = "wwwweeeegtwrewee"
# print(set(str))

# myset = {"cat","cat","dog","pig","rabbit"}
# print(myset)
# myset.add("wolf")   # 往集合中 添加元素add()
# myset.add("lion")
# print(myset)
#
# myset.remove("lion")   # 删除元素 remove()，没有返回值
# print(myset)
#
# element = myset.pop()   # 随机弹出一个元素pop(),有返回值
# print(myset)
# print(element)
#
# myset.clear()  # 清空集合
# print(myset)

# set1 = {1,2,3}
# set2 = {1,3,5}
# print(set1.difference(set2))  # 求集合1和集合2的差集，可以得到新的集合
# print(set1.union(set2))  # 求集合1和集合2的并集
# print(len(set1))  # 求集合的长度


"""
3、统计列表中元素的频率
"""
# list = ['P','p','Y','y','t','t','h','o','o','o','n']
#
# dict ={}
#
# for i in list:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
#
# print(dict)


"""
4、字典的合并
"""
# dict1 = {'a':1,'b':2}
# dict2 = {'c':3,'d':4}
#
# dict1.update(dict2) # 把一个字典的中的键值对 更新到另外一个字典中；不会产生新的字典
# print(dict1)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# print(dict1.get('b'))  # 获取字典中 指定key的值   2
#
# print(dict1.items())  # 以列表的形式返回键和值的元组
# # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
#
# item = dict1.pop('a')  # 删除指定key的键值对  并返回键对应的值
# print(item)
# print(dict1)


"""
5、random模块的使用
"""
# import random
# print(random.random())  # 返回0-1之间的一个随机的浮点数，不带参数
# print(random.randint(1,100))  # 随机生成一个整数类型，可以指定整数的范围
#
# str = '23423423'
# print(random.choice(str)) # 可以从任何序列中，选取一个随机的元素；比如列表、字符串、元组等
#
# print(random.sample(str,3))  # 可以从任何序列中，随机获取指定长度的；


"""
6、检查列表中的元素 的唯一性
思路：将列表的长度 和 set后的长度 做比较，如果相等则说明元素唯一
"""
list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 4, 5, 7]

def ifUnique(seq):

    if (len(seq)) == len(set(seq)):
        print("该列表中元素都是唯一的")
    else:
        print("该列表中元素不是唯一的")

ifUnique(list1)
ifUnique(list2)




