#1 返回字典
def build_person(first_name, last_name):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {"first": first_name, "last": last_name}
    return person
musician = build_person("jimo", "hendrix")
print(musician)

#2 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + " " + last_name
    return full_name.title()
#这是一个无限循环
while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#2.1 使用break语句提供了退出循环
#2 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + " " + last_name
    return full_name.title()
#这是一个无限循环
while True:
    print("\nPlease tell me your name: ")
    print("(enter \'q\' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")