class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print("Hi! I am a Person class!")

    def print_name(self):
        print("Your name is " + self.name)

    def print_age(self):
        print("Your age is " + self.age)