import difflib

def lcs(s1, s2):
  matcher = difflib.SequenceMatcher(None, s1, s2)
  match = matcher.find_longest_match(0, len(s1), 0, len(s2))
  return s1[match.a: match.a + match.size]


n = int(input())
a = input()
if n == 1:
    print(a)
elif n >= 2:
    s = a
    for i in range(n-1):
        b = input()
        b = b
        s = lcs(s, b)
    print(s)
