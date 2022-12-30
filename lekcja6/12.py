import json
xad={
    "book":"witcher",
    "film":"127hours",
    "music":"JWP/BC",
    "series":"TrailerParkBoys",
    "dish":"kanapka z masłem" 
}
with open("favorite.json","w") as f:
    json.dump(xad,f,indent=4)
f.close()
