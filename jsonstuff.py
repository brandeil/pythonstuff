import json

numbers=[2,3,5,7,11,13]

filename='numbers.json'

# store python structures as json data file
with open(filename,'w') as f:
    json.dump(numbers, f)

try:
    with open(filename) as f:
        x=json.load(f)
except:
    print("file not found")
else:    
    print(x)
    