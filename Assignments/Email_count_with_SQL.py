import sqlite3

connection = sqlite3.connect('email_count.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')

cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

filename = input('Enter file name: ')
if (len(filename)< 1): filename = 'Assignment.txt'
file = open(filename)
for line in file:
    if not line.startswith('From: ') : continue
    pieces = line.split()[1]
    org = pieces.split('@')[1]
    #print(org)
    cursor.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cursor.fetchone() 
    if row is None:
        cursor.execute('INSERT INTO Counts(org, count) VALUES (?,1)',(org,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                       (org,))
    connection.commit()
sql = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(sql):
    print(str(row))
    
    
cursor.close()

    