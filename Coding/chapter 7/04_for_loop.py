# l = [1,2,3,4,5,6,7,8,9,0]

# for item in l:
#     print(item)

# for i in range(0,1000,4):
#     print(i) 

table = int(input("Enter the table you want to print : "))

# for i in range(0,20,table):
#     print(f"{table} × {i+1} = {i}")

for i in range(1,21):
    print(f"{table} × {i} = {table * i}")