class Employee:
    componny = "ITC"
    name = "ayushman"
    
    def show(self):
        print(f"The name of the employee {self.name}, company is {self.componny}")


class coder:
    languages = "python"
    
    def printLanguage(self):
        print(f"Your language is {self.languages}")


class Programmer(Employee, coder):  # Inheriting from Employee and coder
    componny = "ITC Infotech"
    
    def showLanguage(self):
        print(f"The name of the employee {self.name}, language he is good at is {self.languages}")


a = Employee()
b = Programmer()
c= coder()



b.show() 
c.printLanguage()            
b.showLanguage()         
