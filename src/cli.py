class CLI:

    def __init__(self, repository):
        self.repository = repository

    def start(self):
        print('Welcome! Choose an action: ')
        continue_loop = True
        while(continue_loop):
            action = input('1: Add a recommendation, 0: Quit ')
            if action=='0':
                break
            if action=='1':
                continue_loop = self.add_new()

    def add_new(self):
        while(True):
            title = input('Title of the item: ')
            while(True):
                check = input(f'Add "{title}" to collection? 1: Yes, 2: No, reinput title, 0: Quit ')
                if check=='1':
                    print(f'"{title}" was added!')
                    return True
                if check=='2':
                    break
                if check=='0':
                    return False
