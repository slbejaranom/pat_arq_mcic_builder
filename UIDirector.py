# "Builder" example.
# This example was elaborated from Partha Kuchana's example of his book "Software Architecture Design Patterns in Java" by Daniel Hernández and
# adapted by Henry Alberto Diosa

class UIDirector():
    def __init__(self, bldr):
        self.__builder = bldr

    def build(self):
        self.__builder.addUIControls()
        self.__builder.initialize()
