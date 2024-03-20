s = input()
t = input()

def checkLetters(s1, t1):
    for i in range(len(s1)):
        if s1[i] == t1[i]:
            return True
    return False

if len(t) > len(s):
    print(0)
else:
    c = 0
    for i in range(len(s) - len(t) + 1):
        if not checkLetters(s[i: i+len(t)], t):
            c += 1
    
    print(c)
