def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enetr the tempreture in farenheit : "))
c= f_to_c(f)
print(f"{f}°F in celcius will be {round(c,2)}°C")
