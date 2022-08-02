for i in range(int(input())):
    conta = input()
    if 'x' in conta: 
        conta = conta.replace('x', '*')
    conta = conta.split('=')
    result_conta = eval(conta[0])
    result_user = int(conta[1])
    if result_conta > result_user:
        qnt = result_conta - result_user
    else:
        qnt = result_user - result_conta
    r = 'r'*int(qnt)
    print(f'E{r}ou!')