import json
with open("makaron.json", "r") as f:
    d=json.load(f)
with open("limited.json","w") as j:
    for i in d:
        j.write(i["first_name"])
        j.write("\n")
        j.write(i["last_name"])
        j.write("\n")
        j.write(str(i["id"]))
        j.write("\n")


