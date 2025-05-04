def greatest(a,b,c):
    if(a>b and a>c):
        return(f"{a} geratesst number")
    elif(a<b and b>c):
        return(f"{b} is a geratest number")
    else:
        return(f"{c} is a geratest number")
    
a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))

print(f"greatest number in {a} ,{b} ,{c} is {greatest(a,b,c)}")
