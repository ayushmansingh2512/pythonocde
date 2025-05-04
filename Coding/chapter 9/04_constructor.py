class Employee:
    Language = "python"
    salary = 1231231

    def __init__(self, name , salary , language): #dundor menthaod which already called
        self.name = name
        self.salary = salary
        self.Language = language
        print("i am creating an obhjject")
    
    def getInfo(self):
        print(f"The language is {self.Language}, the salary is {self.salary}")
    
    
    @staticmethod
    def greet():
        print("good Morning")
    

Ayush = Employee("Ayushman" , 1200000 , "java") 
# Ayush.name = "Ayushman"
print(Ayush.salary, Ayush.Language, Ayush.name)
 