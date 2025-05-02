 
# if(a>=18):
#     print("You are teh above the age of consent \nGood for you")

# elif(a<0):{
#     print("you are entereing invalid age")
# }
# else:
#     print("your are less than 18 \nplses conme back when you are above 18")

# print("end of progarm")
try:
    a = int(input("Enter your age: "))

    if a >= 18:
        print("You are above the age of consent.\nGood for you.")

    elif a < 0:
        print("You are entering an invalid age.")
    
    elif a == 0:
        print("You are entering an invalid age 0.")

    else:
        print("You are less than 18.\nPlease come back when you are above 18.")

except ValueError:
    print("Invalid input. Please enter a valid number.")

print("End of program.")
