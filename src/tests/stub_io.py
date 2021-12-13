
class StubIO:
    """Mocks the functionality of the console IO service"""

    def __init__(self):
        self.inputs = []
        self.outputs = []

    def write(self, message):
        self.outputs.append(str(message).strip())

    def read(self, prompt):
        """Returns a fake input from the input list"""
        self.outputs.append(str(prompt).strip())
        if len(self.inputs) > 0:
            return self.inputs.pop(0)

        raise RuntimeError("IO stub tried to read more values than were available")

    def add_input(self, fake_user_input):
        self.inputs.append(fake_user_input)

    def print_countdown(self, duration):
        for i in reversed(range(duration + 1)):
            self.inputs.append("\rReturning to the main menu in " + str(i) + " seconds")

    def clear(self):
        return
