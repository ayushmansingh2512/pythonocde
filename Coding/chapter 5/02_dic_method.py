marks = {
    "Ayushman" : 100,
    "shubham" : 56,
    "Rohan" : 23,
    0:"Suryansh"    
}

#print(marks.item())
marks.update({"Ayushman" : 99,"sorav" : 100})
print(marks)
print(marks.get("Ayushman"))
