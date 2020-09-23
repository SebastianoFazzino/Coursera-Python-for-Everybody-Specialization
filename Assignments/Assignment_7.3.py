#file_name = input('Enter file name:')
#openfile = open(file_name)
count = 0
tot = 0
openfile = open('Assignment.txt')
for line in openfile:
    if not line.startswith("From ") : continue
    
    result = line.find(':')
    result1 = line[result - 2 : result]
    print(result1)
    
