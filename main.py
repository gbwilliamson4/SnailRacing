import random, time, sys

def main():
    MAX_NUM_SNAILS = 8
    MAX_NAME_LENGTH = 20
    FINISH_LINE = 40

    while True:
        print('How many snails will race? Max:', MAX_NUM_SNAILS)
        response = input('>')
        if response.isdecimal():
            numSnailsRacing = int(response)
            if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
                break
        print('Enter a number between 2 and', MAX_NUM_SNAILS)

    snailNames = []
    for i in range(1, numSnailsRacing + 1):
        while True:
            print(f'Enter snail # {i}\'s name')
            name = input('>')
            if len(name) == 0:
                print('Please enter a name.')
            elif name in snailNames:
                print('Enter a name that hasnt been taken')
            else:
                break
        snailNames.append(name)

    print('\n' * 40)
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
    snailProgress = {}
    for snailName in snailNames:
        print(snailName[:MAX_NAME_LENGTH])
        print('@v')
        snailProgress[snailName] = 0

    time.sleep(1.5)

    while True:
        for i in range(random.randint(1, numSnailsRacing // 2)):
            randomSnailName = random.choice(snailNames)
            snailProgress[randomSnailName] += 1

            if snailProgress[randomSnailName] == FINISH_LINE:
                print(randomSnailName, 'has won!')
                sys.exit()

        time.sleep(0.5)
        print('\n' * 40)

        print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
        print('|' + (' ' * (FINISH_LINE - 1) + '|'))

        for snailName in snailNames:
            spaces = snailProgress[snailName]
            print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
            print(('.' * snailProgress[snailName]) + '@v')


def randomTesting():
    for i in range(100):
        pass

    myNum = random.randint(1, 2 // 2)
    print(myNum)



if __name__ == '__main__':
    main()
    # randomTesting()



