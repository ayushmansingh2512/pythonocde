class Programmer:
    compony = "Microsoft"
    def __init__(self,name, salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Ayushman" , 120000 , 213123)
print(p.name , p.salary,p.pin,p.compony)

r = Programmer("rohaan" , 1200132 , 543123)
print(r.name , r.salary,r.pin,r.compony)