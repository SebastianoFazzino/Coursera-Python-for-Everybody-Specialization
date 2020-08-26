new = dict()
new['money'] = 12
new['candy'] = 3
new['pen'] = 2
print(new)

new['candy'] = new['candy'] + 2
print(new)


counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#get method:

for name in names:
     counts[name] = counts.get(name,0) + 1
print(counts)

#definite for loops and dictionaries:
for key in counts:
    print(key, counts[key])
    
    
#retieving lits of keys and values:
print(list(counts))
print(counts.keys())
print(counts.values)
print(counts.items())

#two iterational variables:
for key, value, in counts.items():
    print(key,value)