print('___________________________________________Star_Pattern___________________________________________\n')

n = int(input("Enter The Number Of Rows"))

for i in range(1,n+1):
    print(" "* (n-i) , end=" ")
    print("*" *(2*i-1), end=" ")
    print("\n")

for i in range(1,n+1):
    
    print("*" *(2*i-1), end="")
    print("\n")