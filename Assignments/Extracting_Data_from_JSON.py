import json
import urllib

URL = input("Enter Location:")
print ("Retrieving", URL)
Json = urllib.request.urlopen(URL)
readData = Json.read()
data = readData.decode()
print ('Retrieved', len(data), 'characters')
json_data = json.loads(data)

sum = 0
totalNum = 0



for item in json_data["comments"]:
    sum += int(item["count"])
    totalNum += 1

print ('Count: ', totalNum )
print ('Sum: ', sum)
