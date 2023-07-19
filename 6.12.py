"""
1. 编写函数Fac(n)，用于求n!，其中n>=0, 并编写测试代码调用该函数。
"""
# def Fac(n):
#     n = int(input("请输入一个大于0的整数："))
#
#     result = 1
#
#     for j in range(2,n+1):
#         result *= j
#
#     print("{}！= {}".format(n,result))
#
# Fac(3)


"""
2.编写程序，生成一个文件，文件名为“学号姓名.txt”（写自己真实的学号和姓名，机器不支持汉字的可以用拼音）；
文件内容为学Python这门课的收获、感想或建议。
"""
# str = '人生苦短，我用python'
#
# f = open('学号姓名.txt','w',encoding='utf-8')   # 创建文件
# f.write(str)  # 写入内容
#
# f.close()  # 关闭文件
#
# print("写入成功")


"""
3.读取一个Python源程序文件“text1.py”，去掉其中的空行和注释行，然后写入另一文件“text2.py”。
"""
# f1 = open('text1.py','r',encoding='utf-8')
# f2 = open('text2.py','w',encoding='utf-8')
#
# line = f1.readlines()  # 读取出来的line 是一个列表
#
# for i in line:
#     if len(i)!=1 and not(i.startswith('#')):
#         f2.write(i)
#
# f1.close()
# f2.close()


"""
4. 编写程序，将九九乘法表按照规范的格式输出到文件“9981.txt”中。
"""
# with open('九九乘法表.txt','w') as f:
#     for i in range(1,10):
#         for j in range(1,i+1):
#             a = "{}*{}={}\t".format(j,i,j*i)
#             print(a,end='')
#             f.write(a)
#
#         print()
#         f.write('\n')



# 总结：文件的相关操作
# file = open('text.py','w')  # open('文件名'，‘模式’)  w是覆盖写入，文件不存在会自动创建
# file.write('423423423423')  # 执行写入动作
#
# file = open('text.py','a')   # 模式a，指的是打开文件的追加模式
# file.write('追加的内容234234234')   # 执行追加操作
#
# file = open('text.py','r')  # 模式r，指的是打开文件的读取模式
# file.read()  # 读取全部
# file.readlines()   # 读取内容，是列表形式





