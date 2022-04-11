class Jedi:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def say_hi(self):
        print('Hello, my name is ', self.name)

    def show_number(self):
        print("Number is: ", self.number)


j = Jedi('ObiWan', 7)
j.say_hi()
j.show_number()
