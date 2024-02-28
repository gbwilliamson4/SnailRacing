

class Snail:
    def __init__(self):
        self.MAX_NAME_LENGTH = 20
        self.name = ""
        self.progress = 0

    def name_snail(self, snailNum):
        # Create the new name and save it in self.name
        while True:  # Keep asking until the player enters a valid name.
            print('Enter snail #' + str(snailNum) + "'s name:")
            name = input('> ')
            if len(name) == 0:
                print('Please enter a name.')
            # elif name in snailNames:
            #     print('Choose a name that has not already been used.')
            else:
                self.name = name
                break  # The entered name is acceptable.

    def progression(self):
        # self.progress = self.progress + 1
        self.progress += 1
