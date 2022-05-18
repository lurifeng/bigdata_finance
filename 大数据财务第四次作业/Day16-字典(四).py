#1 遍历字典中所有的键
favorite_languages = {
    "jen": "python",
    "sarch": "c",
    "edward": "ruby",
    "phil": "python"
}
for name in favorite_languages.keys():
    print(name.title())
print("-------分割线-------")

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
print("-------分割线-------")

#2 按顺序遍历字典中的所有键
favorite_languages = {
    "jen": "python",
    "sarch": "c",
    "edward": "ruby",
    "phil": "python"
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + " ,thank you for taking the poll.")