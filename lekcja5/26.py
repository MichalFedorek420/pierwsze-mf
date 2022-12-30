import re
with open("grades.txt", "r") as f:
    x=re.findall(r'\b\S+\b',f.read())
for i in x:
    if len(i)>=6:
        print(i)

        