

import re
def f3(t): 
    licznik=0
    x = re.findall(r"\d{2,3}", t)
        
    return len(x)

print(f3("Przykładowe liczby parzyste to 16,2,114 oraz 1014, a takze 8"))
