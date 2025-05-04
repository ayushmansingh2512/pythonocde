a = int(input("Enter the nmber you want to chcek ebven or not : "))
try:
    if a%2 == 0:
        print(f"{a} is a even number")
    else:
        print(f"{a} is a odd number")

except(ValueError):
    print("print valaid number")