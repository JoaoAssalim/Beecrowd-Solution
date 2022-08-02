alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(int(input())):
    word = input().upper()
    jump = int(input())
    new_word = ''
    
    for letter in word:
        index = alfabeto.index(letter)
        new_word += alfabeto[index-jump]
        
    print(new_word)