import json

with open("assets/rawdata.json") as f:
    cont = json.load(f)

print(cont)
mercury = None
for x in cont.get("Planets"):
    if x.get("name") == "mercury":
        mercury = x
        break

print(mercury)