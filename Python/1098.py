i = 0
j = 0

while i <= 2:
    aux = j
    for x in range(3):
        aux += 1
        i_str = str(round(i, 1))
        aux_str = str(round(aux, 1))
        
        if i_str[-1] == '0':
            print(f'I={i_str[0]} ', end="")
        else:
            print(f'I={i_str} ', end="")
        if aux_str[-1] == '0':
            print(f'J={aux_str[0]}')
        else:
            print(f'J={aux_str}')
    j += 0.2
    i += 0.2