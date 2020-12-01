
'''
list = open('input.txt').readlines()
list = [item.replace('\n', '') for item in list]
print(list)
listint = [int(i) for i in list]
'''
intlist = []
with open('input') as work_data:
    list = work_data.readlines()

list = [item.replace('\n', '') for item in list]
for ch in list:
    intlist.append(int(ch))



for x in intlist:
    for y in intlist:
        for j in intlist:
            if x + y + j  == 2020:
                print(x*y*j)
                print(x , y, j)


