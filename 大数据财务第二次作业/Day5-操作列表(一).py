#1 遍历整个列表
magicians = ["alice", "david", "carolinsa"]
for magician in  magicians:
    print(magician)
print("-------分隔栏---------")
#1.1 在for循环中执行更多的操作
magicians = ["alice", "david", "carolinsa"]
for magician in  magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")