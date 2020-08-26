#Using split() function with an extern file
openfile = input("Enter file name: ")
file = open(openfile)
for line in file:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
    
    
#double split:
line1 = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:15:23 2020'
words = line1.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])