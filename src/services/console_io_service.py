class ConsoleIOService:
    def write(self, message):
        print(message)

    def read(self, prompt):
        return input(prompt)
