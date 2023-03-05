# "Builder" example.
# This example was elaborated from Partha Kuchana's example of his book "Software Architecture Design Patterns in Java" by Jefferson Jiménez and
# adapted by Henry Alberto Diosa
from SQLBuilderUI import *

class BuilderFactory():
    def getUIBuilder(self,typeL,frame):
        if (typeL==SQLBuilderUI.CANDIDATE):
            return CandSrchBuilder(frame)
        elif (typeL==SQLBuilderUI.EMPLOYER):
            return EmpSrchBuilder(frame)
        return None
