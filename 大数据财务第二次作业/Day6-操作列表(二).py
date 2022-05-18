#1 避免缩进错误
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
print("-------分隔栏---------")
#2 创建数值列表
#2-1 使用函数range()
for value in range(1, 5):
     print(value)
print("-------分隔栏---------")
#2-2 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)
print("-------分隔栏---------")
#2-3 使用range(), 指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print("-------分隔栏---------")
#2-4 将前10个整数的平方加入到一个列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
