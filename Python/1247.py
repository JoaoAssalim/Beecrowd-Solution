while True:
    try:
        D, VF, VG = list(map(int, input().split()))
        hip = (D**2 + 144)**0.5
        
        if (hip/VG) <= (12/VF):
            print("S")
        else:
            print("N")

        
    except EOFError:
        break
