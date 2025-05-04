# contain duplcate with object

class A:
    def containdupli(self, lists):
        seen = set()



        for number in lists:
            if number in seen:
                return True
            
            seen.add(number)
        
        return False
    

a = int(input("Enter the range of number : "))
b = []

for i in range(a):
    number = int(input(f"Enter the number {i+1} : "))
    b.append(number)

sol = A()
result = sol.containdupli(b)

# Print result
if result:
    print("Duplicates found.")
else:
    print("No duplicates found.")