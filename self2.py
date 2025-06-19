#!/usr/bin/python3

class Person:
    def __init__(self, name):  # 'self' refers to the instance being created
        self.name = name

    def say_hello(self):       # 'self' lets the method access instance variables
        print("Hi, I'm", self.name)

p = Person("Alice")
p.say_hello()   # Output: Hi, I'm Alice

