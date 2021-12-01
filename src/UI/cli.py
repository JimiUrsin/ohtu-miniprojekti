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
                continue_loop = self._add_new()
            if action == '2':
                self._browse()

    def _add_new(self):
        while(True):
            title = input('Title of the item: ')
            recom_type = self._input_type()
            while(True):
                check = input(
                    f'Is "{title}", a {recom_type}, correct? 1: Yes, 2: No, reinput information, 0: Quit ')
                if check == '1':
                    self.service.create_new_recommendation(title, recom_type)
                    print(f'"{title}" was added!')
                    return True
                if check == '2':
                    break
                if check == '0':
                    return False

    def _input_type(self):
        type_input = None
        while True:
            type_input = input(
                'Choose the type of the item. 1: book, 2: video, 3: blog, 4: podcast ')
            if type_input == '1':
                return 'book'
            if type_input == '2':
                return 'video'
            if type_input == '3':
                return 'blog'
            if type_input == '4':
                return 'podcast'

    def _browse(self):
        all_items = self.service.get_recommendations()
        if not all_items or len(all_items) < 1:
            print('You have no recommendations saved.')
        else:
            print('You have saved the following recommendations:')
            for title in all_items:
                print(title)
