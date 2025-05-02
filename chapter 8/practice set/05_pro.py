def star(n):
    if(n==0):
        return ""
    print("*" * n)
    star(n-1)

n = int(input("enter the Number of rows : "))
print(star(n))