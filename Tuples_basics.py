#we can put tuples on the left hand side of an
#assignment statement:
    
(x,y) = ('apple',9)
print(y,x)

(a,b,c) = ('orange',99,None)
print(a,b,c)

#we can compare tuples:
print((0,3,5) < (1,8,7))

print((5,6,7) > (6,3,8))

print(('Joe','Hannah') > ('Joe','Bob'))


#Let's sort the tuples inside a dictionary:
d = {'b':1,'a':10,'c':22}
t = sorted(d.items())
print(t)

for k,v in sorted(d.items()):
    print(k,v)
    
#Let's sort them by valus instead of keys:
List = list()    
for k,v in d.items() :
    List.append((v,k))
print(List)
List = sorted(List, reverse = True)
print(List)



