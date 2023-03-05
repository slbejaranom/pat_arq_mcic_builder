# "Builder" example.
# This example was elaborated from Partha Kuchana's example of his book "Software Architecture Design Patterns in Java" by Daniel Hernández and
# adapted by Henry Alberto Diosa
import abc
import time
from tkinter import *
from tkinter import ttk
class UIBuilder:
    __metaclass__ = abc.ABCMeta
    def __init__(self, frame):
        self._searchUI=Frame(frame, bd=2, relief=RIDGE)
    def addUIControls(self):
        raise NotImplementedError()
    def initialize(self):
        raise NotImplementedError()
    def getSQL(self):
        raise NotImplementedError()
    def getSearchUI(self):
        return self._searchUI
#End of class

class CandSrchBuilder(UIBuilder):
    def __init__(self, frame):
        UIBuilder.__init__(self, frame)
        #self._searchUI=Frame(frame, bd=2, relief=RIDGE)
        self.__txtUserName = Entry(self._searchUI)
        self.__txtSkill = Entry(self._searchUI)
        self.__cmbExperience = ttk.Combobox(self._searchUI, state="readonly")
    def addUIControls(self):
        lblUserName = Label(self._searchUI, text="Name: ")
        lblExperienceRange = Label(self._searchUI, text="Experience(min Yrs.)")
        lblSkill = Label(self._searchUI, text="Skill: ")
        self.__cmbExperience["values"] = ["<5",">5"]
        self.__cmbExperience.current(0)
        lblUserName.grid(row=1,column=1,padx=10,pady=10)
        self.__txtUserName.grid(row=1,column=2,padx=10,pady=10)
        lblExperienceRange.grid(row=2,column=1,padx=10,pady=10)
        self.__cmbExperience.grid(row=2,column=2,padx=10,pady=10)
        lblSkill.grid(row=3,column=1,padx=10,pady=10)
        self.__txtSkill.grid(row=3,column=2,padx=10,pady=10)
    def initialize(self):
        self.__txtUserName.insert(0,"")
        self.__txtSkill.insert(0,"Internet Tech")
    def getSQL(self):
        experience = self.__cmbExperience.get()
        return "Select * from Candidate where Username='" + self.__txtUserName.get() + "' and Experience " + experience + " and Skill='" + self.__txtSkill.get() + "'"
        #End of class

class EmpSrchBuilder(UIBuilder):
    def __init__(self, frame):
        UIBuilder.__init__(self, frame)
        #self._searchUI=Frame(frame, bd=2, relief=RIDGE)
        self.__txtUserName = Entry(self._searchUI)
        self.__txtCity = Entry(self._searchUI)
        self.__txtRenewal = Entry(self._searchUI)
    def addUIControls(self):
        self.__lblUserName=Label(self._searchUI,text="Name: ")
        self.__lblCity=Label(self._searchUI,text="City: ")
        self.__lblRenewal=Label(self._searchUI,text="Membership Renewal: ")

        self.__lblUserName.grid(row=1,column=1,padx=10,pady=10)
        self.__txtUserName.grid(row=1,column=2,padx=10,pady=10)
        self.__lblCity.grid(row=2,column=1,padx=10,pady=10)
        self.__txtCity.grid(row=2,column=2,padx=10,pady=10)
        self.__lblRenewal.grid(row=3,column=1,padx=10,pady=10)
        self.__txtRenewal.grid(row=3,column=2,padx=10,pady=10)
        
    def initialize(self):
        self.__txtUserName.insert(0,"")
        currentDate = time.strftime("%B") + "/" +time.strftime("%d" +"/"+ time.strftime("%Y"))
        self.__txtRenewal.insert(0,currentDate)
    def getSQL(self):
        return "Select * from Employer where Username='"+self.__txtUserName.get()+"' and City='"+self.__txtCity.get()+"' and DateRenewal='"+self.__txtRenewal.get()+"'"
#End of class
