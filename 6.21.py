"""
1、怎么让字符的首字母大写，其他字母小写？---------字符串的title方法的应用
"""
# str = 'i loVe pYthon'
# print(str.title())   # title方法可以让单词的首字母大写，其他字母小写


"""
2、怎么在列表末尾加入其他元素？
"""
# list1 = [1,2,3]
# list2 = [4,5,6]
#
# list1.append(5)
# print(list1)    # append添加单个元素  [1, 2, 3, 5]
#
# list1.append([33,44,55])
# print(list1)   # append添加可迭代对象，且不改变添加项的类型 [1, 2, 3, 5, [33, 44, 55]]
#
# list2.extend([555,444,333])
# print(list2)    # extend也可以添加可迭代对象，会改变添加项的类型   [4, 5, 6, 555, 444, 333]

"""
3、有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""
L = [1,2,3,4]
list = []
count = 0

for i in L:
    for j in L:
        for k in L:
            if (i!=j) and (i!=k) and (j!=k):
                result = 100*i + 10*j + k
                list.append(result)
                count += 1

print(list)
print(count)

