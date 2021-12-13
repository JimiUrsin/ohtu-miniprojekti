class CLI:
    """Contains all command line interface functionality"""

    def __init__(self, service, io):
        self.service = service
        self.io = io

    def start(self):
        """Start the main CLI routine."""

        while True:
            self._print_welcome_message()
            action = self.io.read("Your selection: ")
            self.io.clear()

            if action == '0':
                break
            if action == '1':
                self._add_new()
            if action == '2':
                self._browse()
            if action == '3':
                self._edit_or_delete_recommendation()


    def _add_new(self):
        input_for_recommendation = self._ask_for_recommendation_inputs()
        self.service.create_new_recommendation(input_for_recommendation[0], input_for_recommendation[1])
        self.io.write(f'"{input_for_recommendation[0]}" was added!\n\n')
        self.io.print_countdown(3)

    def _ask_for_recommendation_inputs(self):
        """Prompts user to input the title and type of a recommendations.
        Returns a tuple with given title and recommendation type
        """

        while True:
            title = self.io.read('Title of the item: ')
            recom_type = self._input_type()

            check =  self._confirm_user_input(title, recom_type)

            if check:
                return (title, recom_type)

            self.io.clear()


    def _confirm_user_input(self, title, recom_type):
        self.io.clear()

        self.io.write(f'Is "{title}", {recom_type}, correct?')

        self.io.write('\n1: Yes\n'
            '2: No, reinput information\n')

        check = self.io.read('Your selection: ')

        return check == '1'


    def _input_type(self):
        type_input = None

        self.io.write(
            "Choose the type of the item:\n\n"
            "1: book\n"
            "2: video\n"
            "3: blog\n"
            "4: podcast\n"
        )
        while True:

            type_input = self.io.read(
                'Your selection: ')
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
            self.io.write('You have no recommendations saved.')
        else:
            self.io.write('You have saved the following recommendations:')
            self._print_recommendations(all_items)

    def _edit_or_delete_recommendation(self):
        recommendation_chosen_for_editing = self._ask_which_recommendation_to_edit()
        self.io.clear()
        if recommendation_chosen_for_editing:
            self._ask_edit_or_delete_recommendation(
                recommendation_chosen_for_editing[0],
                recommendation_chosen_for_editing[1]
            )

    def _ask_which_recommendation_to_edit(self):
        all_items = self.service.get_recommendations()

        if not all_items or len(all_items) < 1:
            self.io.write("You have no recommendations saved.")
            return None

        self._print_recommendations(all_items, True)
        recommendation_index = self.io.read(
            "Enter the number of the recommendation you would like to edit, or cancel with 0: ")

        # Shift the index one down since we are leaving 0 input for cancel
        recommendation_index_int = int(recommendation_index) - 1

        if recommendation_index_int - 1 < len(all_items) and recommendation_index_int >= 0:
            return (all_items[recommendation_index_int], recommendation_index_int)

    def _ask_edit_or_delete_recommendation(self, recommendation, recommendation_index):
        while True:
            self.io.write(recommendation.title)

            self.io.write("\n1: Edit this recommendation\n"
                          "2: Delete this recommendation\n"
                          "0: Cancel\n")

            action = self.io.read("Your selection: ")

            if action == '0':
                break

            if action == '1':
                (title, recom_type) = self._ask_for_recommendation_inputs()

                success_edit_title = self.service.edit_recommendation_title(title, recommendation_index)
                success_edit_type = self.service.edit_recommendation_type(recom_type, recommendation_index)

                if not success_edit_type or not success_edit_title:
                    self.io.write("Editing Recommendation was not successful")
                break

            if action == '2':
                confirmation = self.io.read("Confirm deletition. 1: Delete, 0: Cancel ")
                if confirmation == '1':
                    success_deletition = self.service.delete_recommendation(recommendation_index)
                    if not success_deletition:
                        self.io.write("Deleting Recommendation was not successful")
                    break

        self.io.print_countdown(5)

    def _print_recommendations(self, recommendations, display_index = False):
        for index, title in enumerate(recommendations):
            recommendation_string = f"{(index + 1)}: {title}" if display_index else title
            self.io.write(recommendation_string)

    def _print_welcome_message(self):
        self.io.clear()
        welcome_text = " Welcome to your Recommendation library! "
        horizontal_bar = "━" * len(welcome_text)

        self.io.write("┏" + horizontal_bar + "┓")
        self.io.write("┃" + welcome_text + "┃")
        self.io.write("┗" + horizontal_bar + "┛")
        self.io.write("Choose an action:\n")

        self.io.write("1: Add a recommendation\n"
                      "2: Browse recommendations\n"
                      "3: Edit or delete recommendations\n"
                      "0: Quit\n")
