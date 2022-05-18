#1 在字典中存储列表（二）
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarch": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"]
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language are: ")
    for language in languages:
        print("\t" + language.title())
print("-------分割线-------")

#2 在字典中存储字典
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton"
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris"
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())