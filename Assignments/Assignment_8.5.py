file_name = input("Enter file name: ")
file = open(file_name)
List = list()
count = 0
for line in file:
     line = line.rstrip()
     words = line.split()
     if len(words) < 3 or words[0] != 'From':
         continue
     if words not in List:
        List.append(words)
        count = count + 1
            
     print(words[1])
print('There were', count, 'lines in the file with From as the first word')            
     