# "Builder" example.
# This example was elaborated from Partha Kuchana's example of his book "Software Architecture Design Patterns in Java" by Jefferson Jiménez and
# adapted by Henry Alberto Diosa

from tkinter import *
from tkinter import ttk
from Builder import *
from BuilderFactory import *
from UIDirector import *


class SQLBuilderUI(Toplevel):
    CANDIDATE = "Candidate SQL Statement"
    EMPLOYER = "Employer SQL Statement"
    EXIT = "Exit"
    GET_SQL = "Show SQL Statement"
    BLANK = ""

    def __init__(self, master):
        Toplevel.__init__(self, master)

        self.__cmbSearchType = ttk.Combobox(self, state="readonly")
        self.__cmbSearchType["values"] = [SQLBuilderUI.BLANK,SQLBuilderUI.CANDIDATE, SQLBuilderUI.EMPLOYER]
        self.__cmbSearchType.current(0)

        self.__txtSQL = Text(self, height=5, width=90)
        self.__txtSQL.insert(END, "The SQL statement will be displayed here.")

        self.__pSearchCriteria = Frame(self, bd=2, relief=RIDGE)

        self.__lblSearchType = Label(self, text="Select SQL Statement:")
        self.__lblWhereClause = Label(self, text="SQL Statement:")
        self.__lblSearchCriteria = Label(self, text="Statement's Criteria:")

        self.__btnGetWhereClause = Button(self, text=self.GET_SQL)
        self.__btnExit = Button(self, text=self.EXIT)

        self.__lblSearchType.grid(row=1, column=1, padx=10, pady=10)
        self.__cmbSearchType.grid(row=1, column=2, padx=10, pady=10)
        self.__lblSearchCriteria.grid(row=2, column=1, padx=10, pady=10)
        self.__pSearchCriteria.grid(row=2, column=2, padx=10, pady=10)
        self.__lblWhereClause.grid(row=3, column=1, padx=10, pady=10)
        self.__txtSQL.grid(row=3, column=2, padx=10, pady=10)
        self.__btnGetWhereClause.grid(row=5, column=1, padx=10, pady=10)
        self.__btnExit.grid(row=5, column=2, padx=10, pady=10)

    def displayNewUI(self, panel):
        self.__pSearchCriteria = None
        self.__pSearchCriteria = panel
        self.__pSearchCriteria.grid(row=2, column=2, padx=10, pady=10)

    def setSQL(self, str):
        self.__txtSQL.delete(1.0, END)
        self.__txtSQL.insert(END, str)

    def getBtnGetWhereClause(self):
        return self.__btnGetWhereClause

    def getBtnExit(self):
        return self.__btnExit

    def getCmbSearchType(self):
        return self.__cmbSearchType

    def getSearchType(self):
        return self.__cmbSearchType.get()


# End of class

class ButtonHandler():
    def __init__(self, root):
        self.__root = root
        self.__frame = SQLBuilderUI(root)
        self.__builder = None
        self.__frame.getBtnGetWhereClause().config(command=self.eventBtnGetWhereClause)
        self.__frame.getBtnExit().config(command=self.eventBtnExit)
        self.__frame.getCmbSearchType().bind("<<ComboboxSelected>>", self.eventCmbSearchType)

    def eventBtnGetWhereClause(self):
        selection = self.__frame.getSearchType()
        if (selection != SQLBuilderUI.BLANK):
            self.__frame.setSQL(self.__builder.getSQL())
        else:
            self.__frame.setSQL("Select one option above")

    def eventCmbSearchType(self, event):
        selection = self.__frame.getSearchType()
        if (selection != SQLBuilderUI.BLANK):
            factory = BuilderFactory()
            self.__builder = factory.getUIBuilder(selection, self.__frame)
            director = UIDirector(self.__builder)
            director.build()
            UIObj = self.__builder.getSearchUI()
            self.__frame.displayNewUI(UIObj)
        else:
            self.__frame.setSQL("You should select one option above")

    def eventBtnExit(self):
        self.__frame.destroy()
        self.__root.destroy()


# End of class

def main():
    root = Tk()
    root.withdraw()
    root.title("Builder example")
    app = ButtonHandler(root)
    root.mainloop()
    # app.frame.mainloop()
    # root.destroy()


if __name__ == "__main__":
    main()
