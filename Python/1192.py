for i in range(int(input())):
    conta = input()
    if conta[0] == conta[-1]:
        print(int(conta[0]) * int(conta[-1]))
    elif conta[0] != conta[-1] and conta[1].isupper():
        print(int(conta[-1]) - int(conta[0]))
    else:
        print(int(conta[-1]) + int(conta[0]))
