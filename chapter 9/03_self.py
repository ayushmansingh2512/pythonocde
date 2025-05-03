class Employee:
    Language = "python"
    salary = 1231231

    def getInfo(self):
        print(f"The language is {self.Language}, the salary is {self.salary}")
    @staticmethod
    def greet():
        print("good Morning")

Ayush = Employee()
Ayush.Language = "Javascript"  # instance attribute
print(Ayush.salary, Ayush.Language)
# Employee.getInfo(Ayush)
Ayush.getInfo()
Ayush.greet()