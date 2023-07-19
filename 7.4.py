# import os
#
# print(os.getcwd())  # 获取当前python脚本的工作目录


import shelve

d = shelve.open('shelve.test') # 打开一个文件

info = {"age":22,"job":'IT'}
name = ["alex","rain","test"]

d["name"] = name
d["info"] = info

d.close()


# 从shelve.test中将内容从小读取出来
d = shelve.open('shelve.test')
print(d.get('name'))
print(d.get('info'))




