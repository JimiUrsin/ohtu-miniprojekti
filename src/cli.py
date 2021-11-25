class CLI:

    def __init__(self, repository):
        self.repository = repository

    def start(self):
        print('Welcome! Choose an action: ')
        while(True):
            action = input('1: Add a recommendation, 0: Quit ')
            if action=='0':
                break
            if action=='1':
                self.add_new()

    def add_new(self):
        while(True):
            title = input('Title of the item: ')
            check = input(f'Add {title} to collection? 1: Yes, 0: No, cancel ')
            if check=='0':
                break
            if check=='1':
                self.repository.add(title)
