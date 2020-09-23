file = open('Assignment.txt')

new = dict()
for line in file:
    line = line.rstrip()
    words = line.split()
    #print(words)
    for w in words:
        if w in new:
            new[w] = new[w] + 1
        else:
            new[w] = 1
            
        #print(w,new[w])
largest = -1
the_word = None
for key, value in new.items():
    #print(key,value)
    if value > largest:
        largest = value
        the_word = key

print(the_word,largest)
