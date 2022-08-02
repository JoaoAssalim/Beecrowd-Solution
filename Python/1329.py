while True:
    times = int(input())
    if times == 0:
        break
    play = input()
    print(f'Mary won {play.count("0")} times and John won {play.count("1")} times')
