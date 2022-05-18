#1 使用列表一部分
#1.1 切片
players = ["charies", "martina", "micheal", "florence", "eli"]
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
print("-------分隔栏---------")

#2 元组
#2.1 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("-------分隔栏---------")
#2.2 遍历元组中的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
print("-------分隔栏---------")
#2.3 修改元组变量
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)