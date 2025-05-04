my_dict = {
        "name":"Ayushman",
        "age": "23"
        }
name = my_dict.get("name")
print(name)

city = my_dict.update({"city":"lucknow"})
print(my_dict)  
food = my_dict.get("pizza")
print(food)  # Output: None
country = my_dict.get("country", "Unknown")
print(country)
