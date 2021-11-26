class Recommendation:
    """
    A single reading / watching / listening recommendation
    """

    def __init__(self, title):
        if len(title) < 1:
            raise Exception("Recommendation has to have a title of at least 2 characters")

        self._title = title

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        if len(new_title) < 1:
            raise Exception("Recommendation has to have a title of at least 2 characters")

        self.title = new_title