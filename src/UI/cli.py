from entities.recommendation import Recommendation


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
        recom_details = self._ask_for_recommendation_inputs()
        try:
            self.service.create_new_recommendation(recom_details)
            self.io.write(f'"{recom_details["title"]}" was added!')
            self.io.print_countdown(3)


        except Exception as error:
            self.io.write(str(error))
            self.io.print_countdown(3)

    def _ask_for_recommendation_inputs(self, recommendation=None, edit=False):
        """Prompts user to input the details for a Recommendation
        The following information is asked for all types:
        (* means this field is mandatory)
            - Title*
            - Author*
            - Comment

        For videos, blogs, and podcasts:
            - URL*

        For books:
            - ISBN

        For books, videos, and blogs
            - Description

        Returns:
            A dictionary with all the mandatory fields as keys with user input as values
            If the user does not input a specific optional field,
            its key will not exist in the dictionary
        """

        while True:
            if edit:
                ask_from_user = self.io.read(f'Current title of the item:  {recommendation.title}, edit = 1: ')
                if ask_from_user == "1":
                    title = self.io.read('New title of the item: ')
                else:
                    title = recommendation.title
            else:
                title = self.io.read('Title of the item: ')

            if edit:
                ask_from_user = self.io.read(f'Current author of the item: {recommendation.author}, edit = 1: ')
                if ask_from_user == "1":
                    author = self.io.read('New author of the item: ')
                else:
                    author = recommendation.author
            else:
                author = self.io.read('Author of the item: ')

            recom_type = self._input_type()

            recom_details = {"title": title, "author": author, "type": recom_type}
            
            if edit:
                self._get_recom_details(recom_details, recommendation, True)
            else:
                self._get_recom_details(recom_details)

            check =  self._confirm_user_input(recom_details)

            if check:
                return recom_details

            self.io.clear()

    def _confirm_user_input(self, recom_details):
        self.io.clear()

        self.io.write("Is the following correct?\n")

        for (key, value) in recom_details.items():
            self.io.write(key.capitalize() + ": " + value)

        self.io.write("\n1: Yes\n2: No, reinput information\n")

        check = self.io.read("Your selection: ")
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

    def _get_recom_details(self, recom_details, recommendation=None, edit=False):
        recom_type = recom_details["type"]

        if recom_type == "book":
            if edit:
                ask_from_user = self.io.read(f"Current ISBN: {recommendation.isbn}, edit = 1: ")
                if ask_from_user == "1":
                    isbn = self.io.read("(Optional) Enter new ISBN: ")
                    recom_details["isbn"] = isbn
                else:
                    isbn = recommendation.isbn
      
            else:
                isbn = self.io.read("(Optional) Enter an ISBN: ")
                if isbn:
                    recom_details["isbn"] = isbn
        else:
            if edit:
                ask_from_user = self.io.read(f"Current URL: {recommendation.url}, edit = 1: ")
                if ask_from_user == "1":
                    url = self.io.read("Enter new URL: ")
                    recom_details["url"] = url
                else:
                    url = recommendation.url  
            
            else:
                url = self.io.read("Enter a URL: ")
    
                recom_details["url"] = url

        if edit:
            ask_from_user = self.io.read(f"Current comment: {recommendation.comment}, edit = 1: ")
            if ask_from_user == "1":
                comment = self.io.read(f"New comment: ")
                recom_details["comment"] = comment
            else:
                comment = recommendation.comment
        else:
            comment = self.io.read("(Optional) Enter a comment: ")
            if comment:
                recom_details["comment"] = comment

        if recom_type != 'podcast':
            if edit:
                ask_from_user = self.io.read(f"Your current description: {recommendation.description}, edit = 1: ")
                if ask_from_user == "1":
                    description = self.io.read("(Optional) Enter new description: ")
                    recom_details["description"] = description
                else:
                    description = recommendation.description
            else:
                description = self.io.read("(Optional) Enter a description: ")
                if description:
                    recom_details["description"] = description

    def _browse(self):
        all_items = self.service.get_recommendations()
        if not all_items or len(all_items) < 1:
            self.io.write('You have no recommendations saved.')
            self.io.print_countdown(3)
        else:
            self.io.write('You have saved the following recommendations:')
            self._print_recommendations(all_items)
            self.io.read("\nPress Enter to return to the main menu")

    def _edit_or_delete_recommendation(self):
        recommendation_chosen_for_editing = self._ask_which_recommendation_to_edit()
        if recommendation_chosen_for_editing:
            self._ask_edit_or_delete_recommendation(
                recommendation_chosen_for_editing[0],
                recommendation_chosen_for_editing[1]
            )
        self.io.print_countdown(3)

    def _ask_which_recommendation_to_edit(self):
        self.io.clear()
        all_items = self.service.get_recommendations()

        if not all_items or len(all_items) < 1:
            self.io.write("You have no recommendations saved.")
            return None

        self._print_recommendations(all_items, True)
        self.io.write("\nEnter the number of the recommendation you would like to edit, or cancel with 0\n")

        recommendation_index = self.io.read("Your selection: ")

        # Shift the index one down since we are leaving 0 input for cancel
        recommendation_index_int = int(recommendation_index) - 1

        if recommendation_index_int - 1 < len(all_items) and recommendation_index_int >= 0:
            return (all_items[recommendation_index_int], recommendation_index_int)

    def _ask_edit_or_delete_recommendation(self, recommendation, recommendation_index):
        while True:
            self.io.clear()
            self.io.write(recommendation.title)

            self.io.write("\n1: Edit this recommendation\n"
                          "2: Delete this recommendation\n"
                          "0: Cancel\n")

            action = self.io.read("Your selection: ")

            if action == '0':
                break

            if action == '1':
                recom_details = self._ask_for_recommendation_inputs(recommendation, True)

                try:
                    self.service.edit_recommendation(recom_details, recommendation_index)
                    self.io.write("Recommendation edited successfully!\n\n")

                except Exception as error:
                    self.io.write(str(error))
                    self.io.print_countdown(3)
                
                break

            if action == '2':
                confirmation = self.io.read("Confirm deletition. 1: Delete, 0: Cancel ")
                if confirmation == '1':
                    try:
                        self.service.delete_recommendation(recommendation_index)
                        self.io.write("Recommendation deleted successfully!\n\n")
                    except Exception as error:
                        self.io.write(str(error))
                    break

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
