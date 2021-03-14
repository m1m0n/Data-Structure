import random

with open("user.txt") as u :
    h = u.readlines()

dic = {}
# dic.update({'name': 'root'})
for i in range(0, len(h)):
    # dic.update({'name' : i.strip()})
    dic[i] = h[i].strip()
print(dic)

