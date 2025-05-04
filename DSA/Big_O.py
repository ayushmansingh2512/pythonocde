print(f"_________________________Big (O) - Linenar Exapmle _________________________________")
print("find 2 in a list if w is there return true else false")

a = int(input("Enter the range of the list : "))

list = []

try:
    for item in range(a):
        number = int(input("Enter the first number : "))
        list.append(number)


    found = False

    for number in list:
        if number == 2:
            found = True
            break # break teh continue
        else:
            continue
    
    print("True" if found else "False")

    

except ValueError:
    print("Please give valid value")

