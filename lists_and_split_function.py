#how to create a list of three elements from a string:
abc = 'a b c'
split_abc = abc.split()
print(split_abc)

sample = 'three different words'
split_sample = sample.split()
print(split_sample)


print(len(split_sample))
print(split_sample[1])


for words in split_sample:
    print(words)
    

#another way of splitting:
line = 'first;second;third;fourth'
split_line = line.split()
print(split_line) 
#doing this way, split() function is not able 
#to split the word in the string.
#so we proceed this way:
proper_split_line = line.split(';')
print(proper_split_line)
#we now have a list with three elements

