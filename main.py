import random, time, sys
from Snail import Snail


def main():
    # Set variables
    MAX_NUM_SNAILS = 8
    FINISH_LINE = 40

    racing_snails = get_number_of_racing_snails(MAX_NUM_SNAILS)
    # Create snail objects and store into list_snails
    list_snails = create_snail_instances(racing_snails)

    # Print the starting point of the race
    print('\n' * 40)
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))

    for snail in list_snails:
        print(snail.name[:snail.MAX_NAME_LENGTH])
        print('@v')
        # snail.progress = 0

    # pause for dramatic effect before we start the game.
    time.sleep(1.5)

    # print_game(numSnailsRacing, snailProgress, snailNames, FINISH_LINE, MAX_NAME_LENGTH)
    print_game(list_snails, FINISH_LINE)

def get_number_of_racing_snails(MAX_NUM_SNAILS):
    while True:
        print('How many snails will race? Max:', MAX_NUM_SNAILS)
        response = input('> ')
        if response.isdecimal():
            numSnailsRacing = int(response)
            if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
                return numSnailsRacing
        print('Enter a number between 2 and', MAX_NUM_SNAILS)

def create_snail_instances(numSnailsRacing):
    # snailNames = []
    snailObjs = []
    for i in range(1, numSnailsRacing + 1):
        # while True:
        snail = Snail()
        snail.name_snail(i)
        snailObjs.append(snail)

    return snailObjs


# def print_game(numSnailsRacing, snailProgress, snailNames, FINISH_LINE, MAX_NAME_LENGTH):
def print_game(list_snails, FINISH_LINE):
    # Main game loop
    while True:
        # pick a random snail and have it progress
        for i in range(random.randint(1, len(list_snails) // 2)):
            randomSnail = random.choice(list_snails)
            # print('randomSnail.progress ', randomSnail.progress)
            randomSnail.progression()

            # Assess if the snail has reached the finish line. If it has, end the game
            if randomSnail.progress == FINISH_LINE:
                print(randomSnail.name, 'has won!')
                sys.exit()

        # Pause between each iteration of the loop
        time.sleep(0.5)
        # This clears out the screen
        print('\n' * 40)

        print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
        print('|' + (' ' * (FINISH_LINE - 1) + '|'))

        for snail in list_snails:
            spaces = snail.progress
            print((' ' * spaces) + snail.name[:snail.MAX_NAME_LENGTH])
            print('.' * snail.progress + '@v')


if __name__ == '__main__':
    main()
    # randomTesting()
