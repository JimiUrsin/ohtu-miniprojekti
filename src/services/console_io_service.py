import time
import os

class ConsoleIOService:
    """Provides functionality for console based input/output from/to the user"""

    def write(self, message):
        """Write a message to the console"""
        print(message)

    def read(self, prompt):
        """Read a line from the user with a given prompt"""
        return input(prompt)

    def print_countdown(self, duration):
        """Prints a countdown of given duration"""
        for i in reversed(range(duration + 1)):
            time.sleep(1)
            print("\rReturning to the main menu in " + str(i) + " seconds", end="", flush=True)

    def clear(self):
        """Clears the console window"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
