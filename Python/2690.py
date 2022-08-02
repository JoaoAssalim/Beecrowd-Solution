for x in range(int(input())):
    ra = ''
    senha = input()
    for i in senha:
        if i == 'G' or i == 'Q' or i == 'a' or i == 'k' or  i == 'u':
            ra += '0'
        elif i == 'I' or i == 'S' or i == 'b' or i == 'l' or  i == 'v':
            ra += '1'
        elif i == 'E' or i == 'O' or i == 'Y' or i == 'c' or  i == 'm' or i == 'w':
            ra += '2'
        elif i == 'F' or i == 'P' or i == 'Z' or i == 'd' or  i == 'n' or i == 'x':
            ra += '3'
        elif i == 'J' or i == 'T' or i == 'e' or i == 'o' or  i == 'y':
            ra += '4'
        elif i == 'D' or i == 'N' or i == 'X' or i == 'f' or  i == 'p' or i == 'z':
            ra += '5'
        elif i == 'A' or i == 'K' or i == 'U' or i == 'g' or  i == 'q':
            ra += '6'
        elif i == 'C' or i == 'M' or i == 'W' or i == 'h' or  i == 'r':
            ra += '7'
        elif i == 'B' or i == 'L' or i == 'V' or i == 'i' or  i == 's':
            ra += '8'
        elif i == 'H' or i == 'R' or i == 'j' or i == 't':
            ra += '9'
        
    if len(ra) > 12:
        print(ra[:12])
    else:
        print(ra)