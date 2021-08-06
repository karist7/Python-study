character = {
    "name": "기사",
    "level" : 12,
    "items" : {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
 }

for key in character:
    if type(character[key]) is dict:
        for keys in character[key]:
            print(keys)
            print(keys, ":", character[key][keys])
    elif type(character[key]) is list:
        for keys in character[key]:
            print(keys)
            print(key, ":", keys)
    else:
        print(key, ":", character[key])
