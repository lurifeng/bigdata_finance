#2 将函数存储在模块中
#2.1 导入整个模块
def make_pizza(size, *toppings):
    '''概述要制作的披萨'''
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)