def sum(n):
    if(n==1 or n==0):
        return 1
    return n + sum(n-1)

n = int(input("Enter the number : "))
print(f"the sum of {n} will be {sum(n)} ")
    