"""
1. 写一个程序，生成一个随机数并将其逆序输出
"""
# import random
# num = random.randint(1,1000)
# print(num)
# print(str(num)[::-1])


"""
2. 写一个程序，将两个列表合并成一个有序的列表
"""
# list1 = [2,3,1,5]
# list2 = [9,5,2,6]
# print(sorted(list1 + list2))   # 将列表拼接后，可以用sorted()方法 进行排序，默认升序



"""
3. 写一个程序，找出两个列表中的相同元素
思路：求和、求差、求全集 等程序，考虑用集合实现
"""
# list1 = [2,3,1,5]
# list2 = [9,5,2,6]
#
# print(set(list1) & set(list2))  # 求和 用&
# print(set(list1) ^ set(list2))   # 求差集，用^
# print(set(list1) | set(list2))    # 求并集，用|



"""
4. 写一个程序，将一个字符串中的所有字母小写并去除空格
"""
# string = "RUUEREU  RIWERUER REIRUWE  IRWERWE"
#
# new_string = string.lower().replace(" ","")
# print(new_string)

"""
5. 写一个程序，计算一个数的阶乘
"""
def fact(n):

    result = 1

    for i in range(1,n+1):
        result *= i

    print(result)

fact(10)











