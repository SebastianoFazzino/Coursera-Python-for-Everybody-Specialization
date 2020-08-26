#how to find the most common word in a text:

openfile = input("Enter file name: ")
file = open(openfile)
counts = dict()

for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
   if bigcount is None or count > bigcount:
      bigword = word
      bigcount = count
        
       
print(bigword,bigcount)




