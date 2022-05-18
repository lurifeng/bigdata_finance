#1 使用标志
prompt = "\nTell me something, and I will repeat it back to you!"
prompt += "\nEnter \'quit\' to end the program."
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

#2 使用break退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter \'quit\' when you are finished.)"
active = True
while active:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")
