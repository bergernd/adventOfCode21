w = open('test.txt', 'r')

oxy = [x.strip() for x in w]
co2 = oxy[:]
#print(co2)

count = 0
while len(oxy) > 1:
    totals = [0,0]
    for x in oxy:
        if x[count] == '1':
            totals[1]+=1
        else:
            totals[0]+=1
    if totals[1] >= totals[0]:
        oxy = [x for x in oxy if x[count] == '1']
    else:
        oxy = [x for x in oxy if x[count] == '0']
    count += 1
#print(oxy)
#print(co2)
count = 0
while len(co2) > 1:
    totals = [0,0]
    for x in co2:
        if x[count] == '1':
            totals[1]+=1
        else:
            totals[0]+=1
    if totals[1] >= totals[0]:
        co2 = [x for x in co2 if x[count] == '0']
    else:
        co2 = [x for x in co2 if x[count] == '1']
    count += 1
print(co2)

print(int(oxy[0],2))
print(int(co2[0],2))
