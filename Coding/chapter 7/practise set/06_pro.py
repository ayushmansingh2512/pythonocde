print("___________________________________________________________Factorial number___________________________________________________________")

num = int(input("enter the number : "))
fact = 1
if(num < 0):
    print("Factorial number are not negative ")
else:
    for i in range(1, num+1):
        fact *= i
    print(f"The factorial of {num} is {fact}")
