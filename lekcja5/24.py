import re
tekst="To be, or not to be, that is the question"


x=re.findall(r'[aeioyu]', tekst)

print(len(x))
