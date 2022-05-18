#1 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print("-------分割线-------")

#2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != "quit":
    message = input(prompt)
    print(message)
print("-------分割线-------")

#2.1 使用一个简单的if测试
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
