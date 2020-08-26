#building a list:
    
stuff = list()
stuff.append('book')
stuff.append('99')
print(stuff)


#is something in a list?
somethings = [1,9,21,10,16]
print(9 in somethings, 15 in somethings, 20 not in somethings)


#ordering in a list:
somethings.sort()    
print(somethings)
print(somethings[1])

#built-in functions and lists:
print(len(somethings))
print(max(somethings))
print(min(somethings))
print(sum(somethings))
print(sum(somethings)/len(somethings))



#building a list with a while loop:
numlist = list()
while True:
    Input = input('Enter a number: ')
    if Input == 'done': break
    value = float(Input)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('average = ', average)
print('biggest number = ',max(numlist))
print('smallest number = ',min(numlist))