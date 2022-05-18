#1 位置实参
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("hamster", "harry")
describe_pet("dog", "willie")

#2 位置实参的顺序很重要
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("harry", "hamster")

#3 关键字实参
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type = "hamster", pet_name = "harry")
describe_pet(pet_name = "harry", animal_type = "hamster")