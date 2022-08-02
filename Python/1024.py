for i in range(int(input())):
    word = input()
    encrypted_msg = ''
    for char in word:
        if char.isalpha():
            encrypted_msg += chr(ord(char)+3)
            continue
        encrypted_msg += chr(ord(char))
    encrypted_msg = list(encrypted_msg[::-1])

    first_part = encrypted_msg[:int(len(encrypted_msg)/2)]
    second_part = encrypted_msg[int(len(encrypted_msg)/2):]
    for i in range(len(second_part)):
        second_part[i] = chr(ord(second_part[i])-1)
        
    print(str(''.join(first_part)+''.join(second_part)))