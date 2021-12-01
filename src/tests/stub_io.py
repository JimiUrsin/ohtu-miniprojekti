
class StubIO:
    def __init__(self):
        self.inputs = []
        self.outputs = []
    
    def write(self, message):
        self.outputs.append(message.strip())
    
    def read(self, prompt):
        self.outputs.append(prompt.strip())
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            raise RuntimeError("IO stub tried to read more values than were available")

    def add_input(self, input):
        self.inputs.append(input)
