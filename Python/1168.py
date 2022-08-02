leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


for i in range(int(input())):
    total = 0
    ent = input()
    for led in ent:
        total += leds[int(led)]
    print(f'{total} leds')