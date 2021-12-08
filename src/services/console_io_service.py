class ConsoleIOService:
    """Provides functionality for console based input/output from/to the user"""

    def write(self, message):
        """Write a message to the console"""
        print(message)

    def read(self, prompt):
        """Read a line from the user with a given prompt"""
        return input(prompt)
