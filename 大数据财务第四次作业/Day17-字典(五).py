#1 遍历字典中的所有值
favorite_languages = {
    "jen": "python",
    "sarch": "c",
    "edward": "ruby",
    "phil": "python"
}
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
print("-------分割线-------")

for language in set(favorite_languages.values()):
    print(language.title())
print("-------分割线-------")

#2 字典列表
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print("-------分割线-------")

aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))