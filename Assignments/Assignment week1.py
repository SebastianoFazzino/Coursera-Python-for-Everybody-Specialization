num = 0
tot = 0
while True:
    value = input("Enter a number: ")
    if value == 'done':
        break
    try:
        new_value = float(value)
    except:
        print("invalid input")
        continue
    
 #print(new_value)
    num = num + 1
    tot = tot + new_value
#print('All done!!')
print(num,tot,tot/num)



largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
        
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num
    
    

print("Maximum is", largest)
print("Minimum is", smallest)