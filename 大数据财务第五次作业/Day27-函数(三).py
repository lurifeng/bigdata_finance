#1 默认值
def describe_pet(pet_name, animal_type="dog"):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name="willie")
describe_pet("willie")

#2 等效的函数调用
# 一条名为Willie的小狗
describe_pet("willie")
describe_pet(pet_name="willie")

# 一只名为Harry的仓鼠
describe_pet("harry", "hamster")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")
