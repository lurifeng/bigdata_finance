#1 由类似对象组成的字典
favorite_languages = {
    "jen": "python",
    "sarch": "c",
    "edward": "ruby",
    "phil": "python"
}
print("Sarah's favorite language is " + favorite_languages["sarch"].title() + ".")
print("-------分割线-------")
#2 遍历字典
user_0 = {
    "username": "efermi",
    "first": "enrice",
    "lasr": "fermi"
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print("-------分割线-------")

favorite_languages = {
    "jen": "python",
    "sarch": "c",
    "edward": "ruby",
    "phil": "python"
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
