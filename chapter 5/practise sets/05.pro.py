d={}

a = int(input("Enter the number of freinds do you have : "))

for i in range(a):
    name = input("Enter the name of freind : ")
    lang = input("Enter the language : ")
    d.update({name:lang})

print("Your freind are")
for name in d:
    print(f"{name} work in {lang} ")

print(d)
