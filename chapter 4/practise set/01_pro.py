# city = input("Enter the name of seven fruits sepreaatedd by spaces")
# input_list= city.split()
# print(input_list)
 
city2 = input("Enter the number of cities you want : ")

try:
    num_cities = int(city2)
    my_list = []
    for i in range(num_cities):
        item = input(f"City name {i+1}: ")
        my_list.append(item)
    print(my_list)
except ValueError:
    print("Invalid input. Please enter a whole number for the number of cities.")