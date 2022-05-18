#1 列表
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0]) #1-1 打印第一个元素
print(bicycles[1]) #1-2 打印第四个元素
print(bicycles[-1]) #1-3 打印最后一个元素
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message) #1-4 使用列表中的各个值
print("-------分隔栏---------")
#2 修改列表元素
motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)
motocycles[0] = "ducati"
print(motocycles)
print("-------分隔栏---------")
#3 在列表中添加元素
#3-1 在列表末尾添加元素
motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)
motocycles.append("ducati")
print(motocycles)
#3-2 在列表中插入元素
motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)
motocycles.insert(0, "ducati")
print(motocycles)