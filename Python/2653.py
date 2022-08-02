joias = []

while True:
    try:
        joia = input()
        if joia not in joias:
            joias.append(joia)
        
    except EOFError:
        break
print(len(joias))
