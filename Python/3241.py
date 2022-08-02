for i in range(int(input())):
    calc = input()
    if calc == 'P=NP':
        print('skipped')
    else:
        print(eval(calc))