class CLI:

    def __init__(self, service):
        self.service = service

    def start(self):
        print('Welcome! Choose an action: ')
        continue_loop = True
        while(continue_loop):
            action = input(
                '1: Add a recommendation, 2: Browse recommendations, 0: Quit ')
            if action == '0':
                break
            if action == '1':
                continue_loop = self.add_new()
            if action == '2':
                self.browse()

    def add_new(self):
        while(True):
            title = input('Title of the item: ')
            while(True):
                check = input(
                    f'Add "{title}" to collection? 1: Yes, 2: No, reinput title, 0: Quit ')
                if check == '1':
                    self.service.create_new_recommendation(title)
                    print(f'"{title}" was added!')
                    return True
                if check == '2':
                    break
                if check == '0':
                    return False

    def browse(self):
        all_items = self.service.fetch_all()
        print('You have saved the following recommendations:')
        for title in all_items:
            print(title)
