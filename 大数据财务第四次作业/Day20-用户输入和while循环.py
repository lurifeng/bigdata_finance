#1 函数input()的工作原理
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
print("-------分割线-------")

#1.1 编写清晰的程序
name = input("Please enter your name: ")
print("Hello, " + name + "!")
print("-------分割线-------")

#1.1.1
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
print("-------分割线-------")

#1.2 使用int()来获取数值输入
age = input("How old are you? ")
print(age)
print("-------分割线-------")

#1.2.1
age = input("How old are you? ")
age = int(age)
print(int(age) >= 18)
print("-------分割线-------")

#1.2.2
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
print("-------分割线-------")

#1.3 求模运算符
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)
print("-------分割线-------")

#1.3.1
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")