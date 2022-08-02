seg = int(input())
horas = seg//3600
seg-=(horas*3600)
minu = seg//60
seg -= (minu*60)

print(f'{horas}:{minu}:{seg}')