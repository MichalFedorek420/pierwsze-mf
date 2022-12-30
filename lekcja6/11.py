import json
with open("data.json") as f:
    d=json.load(f)
for i in range(len(d)):
    for keys,values in d[i].items():
        print(keys,":",values)

