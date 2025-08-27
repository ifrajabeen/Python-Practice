dis = {
    'name':"ifra",
    "age" : 21,
    "phone" : "vivo y33s",
    "phone" : "vivo y21" #overwrite kary ga
    
}
# print(dis)
# print(dis['name'])
# print(dis.get('phone','not found'))
# print(dis.keys())
# print(dis.values())
# print(dis.items())
# print(dis.update({"year":2023}))
# dis.pop("age") #remove the key and value
# print(dis)

# for key in dis.keys():
#     print(f"the value corresponding to the key {key} is {dis[key]}")

for key,value in dis.items():
    print(f"the value corresponding to the key {key} is {value}")