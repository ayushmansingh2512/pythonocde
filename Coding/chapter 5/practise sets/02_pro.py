unique_num = set()

a= int(input("Enter how many number you are going to give :" ))


for i in range(a):
    num = int(input(f"enter the number {i+1} :"))
    unique_num.add(num)

print("\nUnique number entered are :") 
for num in unique_num:
    print(num)
print(unique_num)


