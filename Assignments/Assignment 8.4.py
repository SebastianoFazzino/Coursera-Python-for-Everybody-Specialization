file_name = input("Enter file name: ")
file = open(file_name)


List = list()
for line in file:
     line = line.rstrip()
     words = line.split()
     for word in words:
         if word  not in List:
             List.append(word)
             
    
         

List.sort()
print(List)
       