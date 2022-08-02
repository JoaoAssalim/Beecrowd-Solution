def subs(x):
  if not x[0].isnumeric():
    return x[0]+str(int(x[1:]))
  return x

i=1
while True:
  n = input()
  if n=="0":
    break

  a = input()
  b = a.replace("+"," +").replace("-"," -").split()
  c = "".join(map(subs,b))
  print("Teste {}".format(i))
  print(eval(c))
  print()
  i+=1