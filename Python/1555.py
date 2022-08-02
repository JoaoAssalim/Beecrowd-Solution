def r(x,y):
    return (3*x)**2 + y**2
def b(x,y):
    return 2*(x**2) + (5*y)**2
def c(x,y):
    return -100*x + y**3
    
for i in range(int(input())):
    x,y = list(map(int, input().split()))
    rafa = r(x,y)
    beto = b(x,y)
    carlos = c(x,y)
    
    if rafa > beto and rafa > carlos: print('Rafael ganhou')
    elif beto > rafa and beto > carlos: print('Beto ganhou')
    elif carlos > rafa and carlos > beto: print('Carlos ganhou')