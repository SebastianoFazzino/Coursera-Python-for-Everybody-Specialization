x =[1,55,68.45,7895,332,253,45,61,6789,124,614,2525,552,8561,456,655,518]


largest = 1
print("before",largest)

for num in x:
    if num > largest:
        largest = num
    print(largest, num)  
print("after",largest)



count = 0
for item in x:
    count = count +1
print(count)


SUM = 0
for num in x:
    SUM = SUM + num
print(SUM)


Sum = 0
Count = 0
for i in x:
    Count = Count + 1
    Sum = Sum + i
    print(Count,Sum,i)
    