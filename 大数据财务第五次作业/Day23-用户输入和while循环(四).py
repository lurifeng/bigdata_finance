#1 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#1.1 避免无限循环
x = 1
while x <= 5:
    print(x)
    x += 1

#2 在列表之间移动元素
# 首先创建一个待验证的用户列表
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())