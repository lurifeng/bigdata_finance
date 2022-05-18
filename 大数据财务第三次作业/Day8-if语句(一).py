cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#2 条件测试
#2.1 检测是否相等
car = "bmw"
car == "bmw"

car = "Audi"
car == "audi"

car = "Audi"
car.lower() == "audi"

car = "Audi"
car.lower() == "audi"
car
print('--------分割线--------')

#3 检查是否不相等
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

print('--------分割线--------')
