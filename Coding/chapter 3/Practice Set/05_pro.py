print("Enter your details")

f_name = (input("Enter your First name : "))
l_name = (input("Enter your Last name : "))

a = f_name.title()
b = l_name.title()

age = (input("Enter your age : "))
Gender = (input("Enter your gender for Male press M for Female press F :"))

location = (input("enter your address :"))
fav_sub = (input("enter your fav sunject : "))
fav_emoji =(input("enter your fav emoji : "))
print("__________________________________________________________________________________________________________________________")
print("Personalized Email Generator")
print(f"Hello {a} {b} \nThank you for signing on oour platform \nHere are some detail we have gathered: \nAge : {age}")
if(Gender == "M"):
    print(f"Gneder:Male")
elif(Gender == "F"):
    print(f("Gender:Female"))
else:
    print("not specified")
print(f"Loaction:{location.title()} \nFav subject:{fav_sub} \nFav emoji:{fav_emoji}")
