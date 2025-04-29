# tuples are imputable
a = (1,2,3,4,5)
b=()# empty tuple
c=(1,) #tuple with one element
t = type(a)
print(a, t)

s = ["apple" , "orange" , "surayansh" , "sorav" , False , 231.3 ,4 ,"Aditya"]
no = a.count(4)
i = s.index(4)
print(f"{no} , {i}")

x =(1,2.6,9,65,89,90)
y=(3,4,5,43,152,213)
z= x+y
print(f"the original tuple is {z}")
listz = list(z)
listz.sort()
sortedTuplez = tuple(listz)
print(sortedTuplez)
print(len(sortedTuplez))

