while True:
    try:
        conv = ''
        real = input()
        centavos = input()
        
        if len(real) % 3 == 0:
            i = 0
            v = 1
            sobra = 0
            while sobra < len(real):
                if i == 3 and v == 1:
                    conv += ','
                    i = 0
                    v += 1
                elif i == 3:
                    conv += '.'
                    i= 0
                    
                conv += real[sobra]
                sobra += 1
                i += 1
            
            if len(centavos) != 2:
                centavos = "0" + centavos
            conv += f'.{centavos}'
            while conv.count(".") > 1:
                conv = conv[:conv.index('.')] + "," + conv[conv.index('.')+1:]
            print("$"+conv)
            
        else:
            sobra = len(real) % 3
            if len(real) > 2:
                if int(real[:sobra]) != 0:
                    conv += f'{real[:sobra]},'
            else:
                conv += f'{real[:sobra]}'
            
            i = 0
            while sobra < len(real):
                if i == 3:
                    conv += '.'
                    i = 0
                conv += real[sobra]
                sobra += 1
                i += 1
            
            if len(centavos) != 2:
                centavos = "0" + centavos
            conv += f'.{centavos}'
            
            while conv.count(".") > 1:
                conv = conv[:conv.index('.')] + "," + conv[conv.index('.')+1:]
            print("$"+conv)
    except EOFError:
        break