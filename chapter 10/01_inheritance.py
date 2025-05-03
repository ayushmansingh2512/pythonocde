class Employee:
    componny = "ITC"
    def show(self):
        print(f"the name of the employee {self.name} salary is {self.salary}")


# class Programmer:
#     compony = "ITC Infotexh"
#     def show(self):
#         print(f"the name of the employee {self.name} salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f"the name of the employee {self.name}  lang he is good at is {self.language}")


class Programmer(Employee): #base class
    compony = "ITC Infotexh"
    def showLanguage(self):
        print(f"the name of the employee {self.name}  lang he is good at is {self.language}")
    

a = Employee()
b = Programmer()

print(a.componny,b.compony)