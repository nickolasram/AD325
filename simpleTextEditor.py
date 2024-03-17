class TextOperation:
    def __init__(self, operation, text=None):
        self.operation = operation
        self.text = text


class TextEditor:
    def __init__(self):
        self.stack = []

    def retrieveText(self):
        output = ""
        for i in self.stack:
            if i.operation == "Add":
                output = output + i.text
            else:
                output = output[:-1]
        return output

    def display(self):
        print(self.retrieveText())

    def addText(self, character):
        self.stack.append(TextOperation("Add", character))
        self.display()

    def undo(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.display()

    def delete(self):
        self.stack.append(TextOperation("Del"))
        self.display()