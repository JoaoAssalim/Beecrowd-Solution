p = [["E", "C", "A", "F"]]
b = 0
for i in range(int(input())):
    s = input().split()
    if s == p[-1]:
        b += 1
        p.pop()
    else:
        p.append(s[::-1])
    
    if not p:
        p.append(["E", "C", "A", "F"])

print(b)
