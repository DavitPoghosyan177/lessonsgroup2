#19
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = d2
for i , j in d1.items():
    if i in d2:
        d3[i] = j+d2[i]
    else:
        d3[i] = j
            
print(d3)

#23

diclst =  [{'item': 'item1', 'amount': 400}, 
           {'item': 'item2', 'amount': 300}, 
           {'item': 'item1', 'amount': 750}]
md={}
for i in diclst:
    if i['item'] not in md:
        md[i['item']] = i['amount']
    else:
        md[i['item']] += i['amount'] 
print(md) 

#30

shoptop = {'item1': 45.50, 
           'item2':35,
           'item3': 41.30,
           'item4':55,
           'item5': 24}
d = {}
val=list(shoptop.values())
val.sort()
val.reverse()
nval=val[:3]
for i in nval:
    for j in shoptop.keys():
        if(shoptop[j]==i):
            print(j , shoptop[j])

#10 list

mstr = input("Enter the string: ")
n = int(input("Enter the lenght: "))
mstr1 = mstr.split()
ml = []
for i in mstr1:
    if len(i) > n:
        ml.append(i)
print(ml)

#11 list 

lst1 = [1 , 2 , 3 , 4]
lst2 = [5 , 6 , 7 , 4]
for i in lst1:
    for j in lst2:
        if i == j:
            print("True")
            break
     
#12 list

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
ml = []
for i in color_list_1:
    if i not in color_list_2:
        ml.append(i)
print(ml)