def verifica_triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "Invalido"
    if a == b == c:
        tipo = "Equilatero"
    elif a == b or a == c or b == c:
        tipo = "Isoceles"
    else:
        tipo = "Escaleno"
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        retangulo = "S"
    else:
        retangulo = "N"

    return "Valido-" + tipo + "\nRetangulo: " + retangulo


A, B, C = map(int, input().split())
print(verifica_triangulo(A, B, C))
