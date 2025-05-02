print("______________________________________Print the table Using While loop______________________________________\n")
table = int(input("Enter number you want table of : "))
print(f"Here the table of {table} using while-loop\n")

i = 0
while(i<20):
    i = i+1
    
    print(f"{table} × {i} = {table*i}\n")
