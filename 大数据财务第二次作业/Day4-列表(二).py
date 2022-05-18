#1 从列表中删除元素
#1-1 使用del语句删除元素
motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)
del motocycles[0]
print(motocycles)
print("-------分隔栏---------")
#1-2 使用pop()删除元素
motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)
popped_motorcyle = motocycles.pop()
print(motocycles)
print(popped_motorcyle)
print("-------分隔栏---------")
#1-3 弹出列表中任何位置处的元素
motocycles = ["honda", "yamaha", "suzuki"]
first_owned = motocycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print("-------分隔栏---------")
#1-4 根据值删除元素
motocycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motocycles)
motocycles.remove("ducati")
print(motocycles)
print("-------分隔栏---------")
#2 组织列表
#2-1 使用方法sort()对列表进行永久性排序
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort() #正序
print(cars)
cars.sort(reverse = True) #反序
print(cars)
print("-------分隔栏---------")
#2-2 使用函数sorted()对列表进行临时排序
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list: ")
print(cars)
print("Here is the sorted list: ")
print(sorted(cars))
print("Here is the original list again: ")
print(cars)
print("-------分隔栏---------")
#2-3 倒着打印列表reverse()
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)
print("-------分隔栏---------")
#2-4 确定列表长度
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))