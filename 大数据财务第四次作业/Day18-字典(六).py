#1 字典列表（二）
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(0, 30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[0: 3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
print("-------分割线-------")

#添加一个elif代码块
aliens = []
for alien_number in range(0, 30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[0: 3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
#把黄色外星人改为移动速度快且值为15个点的红色外星人
for alien in aliens[0: 5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
for alien in aliens[:5]:
    print(alien)
print("...")
print("-------分割线-------")

#2 在字典中存储列表
# 存储所点的披萨信息
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}
# 概述所点的披萨
print("You ordered a " + pizza["crust"] + "-curst pizza " + "with the following toppings: ")
for topping in pizza["toppings"]:
    print("\t" + topping)