#1 使用if语句（一）
age = 19
if age >= 19:
    print("You are old enough to vote!")
#1.1 if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#1.2 if-elif-else结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#简化语句
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 0
print("Your admission cost is $" + str(price) + "." )