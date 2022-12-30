with open("shoppinglist.txt","w") as k: 
    with open("GrainAndBread.txt","r") as f:
        with open("MeatAndFish.txt", "r") as g:
            for i in f:
                k.write(i)
            for i in g:
                k.write(i)