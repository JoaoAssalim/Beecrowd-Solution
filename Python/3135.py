s = {}
for i in range(int(input())):
    x = input()
    if len(x) in s:
        s[len(x)].append(x)
    else:
        s[len(x)] = [len(x), x]

clas = [s[key] for key in s.keys()]
clas.sort()

while any(len(i) > 1 for i in clas):
    st = []
    for i in clas:
        if len(i) > 1:
            st.append(i[1])
            i.remove(i[1])
    
    print(", ".join(st))
    
