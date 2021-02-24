a = '''
Игорь телевизор 1
Маша гитара 2
Игорь кружка 12
Алина наушники 3
'''.split()
cop = a
list_1 = []
list_2 = []
shop = {1: {'customer': 'name', 'item': 'name', 'number': 0}, 2: {'customer': 'name', 'item': 'name', 'number': 0},
        3: {'customer': 'name', 'item': 'name', 'number': 0}, 4: {'customer': 'name', 'item': 'name', 'number': 0}}


for i in shop:
    for step in shop[i]:
        shop[i][step] = cop[0]
        cop.remove(cop[0])



print(shop)

for i in shop:
    list_1.append(shop[i]['customer'])

for step in range(len(list_1)):
    for i in shop:
        if shop[i]['customer'] == list_1[step]:
            list_2.append(shop[i]['item'] + shop[i]['number'])

print(list_1)
print(list_2)
