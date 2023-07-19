"""
1、三数排序：输入三个整数x、y、z，请把这三个数有小到大输出；
"""
# raw = []
#
# for i in range(3):
#     n = int(input("请输入一个整数"))
#     raw.append(n)
#
# print(sorted(raw))  # 可以直接调函数进行排序
#
# 方法二：
# for i in range(0,len(raw)):
#     for j in range(1,len(raw)):
#         if raw[i] > raw[j]:
#             raw[i],raw[j] = raw[j],raw[i]
#
# print(raw)


"""
2、从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件“test”中保存；
"""
if __name__ == "__main__":
    f = open('test.txt','w')
    string = input("请输入一个字符串：")
    new_string = string.upper()
    f.write(new_string)

    f.close()








