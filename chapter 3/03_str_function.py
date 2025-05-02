name = "Ayushman"
name2 = "namasya"
title = "hello world"
print(len(name))
print(name.endswith("man")) # str end with "man" that why output is true its alos case senstive
print(name.startswith("ayus")) # false wbeacuse a is written in small
print(name.startswith("Ayus"))# will give true start with A 

print(name2.capitalize()) #starting word becomae capital 
print(title.title()) # make both first word capital of a string 

s = "ayushman singh is good"
print(s.replace("good" , "bad"))
