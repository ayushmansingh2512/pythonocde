print("________________________________________________Prime Number________________________________________________\n")

num = int(input("enter the number : "))

if num<2:
    print("Not a prime number")
else:
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            print("not a prime number")
            break
    else:
        print("prime numebr")
