#1 一个简单的字典
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

#2 使用字典
ailen_0 = {"color": "green", "points": 5}
#2.1 访问字典中的值
alien_0 = {"color": "green"}
print(alien_0["color"])

#
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print("You just earned " + str(new_points) + "points!")

#2.2 添加键-值对
alien_0 = {"color": "green", "points": 5}
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
#2.3 先创建一个空字典
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)