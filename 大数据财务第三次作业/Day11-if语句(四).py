#1 使用if语句（二）
#1.1 使用多个elif代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    print = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
#1.2 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
#1.3 测试多个条件
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
#1.3.1 
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")