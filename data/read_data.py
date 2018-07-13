import json

filename = "Books_5.json"
data = []
count = 0
with open(filename, 'r') as f:
    for line in f:
        data.append(json.loads(line))
        print line
        count += 1
        if (count > 100): break;
# print data
