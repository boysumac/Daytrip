greeting = "Hi there"

print(greeting)

import random

# list of destinations
destinations = ['Milwaukee', 'Door County', 'Madison', 'Crivitz']    

# list of restaurants
restaurants = ['Shakers', 'Lakeside', 'Antlers', 'Nitty Gritty']

# list of transportation
transportation = ['train', 'bus', 'RV', 'Harley']

# list of entertainment
entertainment = ['concert', 'comedy act', 'boat ride', 'hike']

# Create Dictionary

# Determine destination with user input

valid_response = "no"

while valid_response == "no":

    destination = random.choice (destinations)
    destination_input = input(f"Would you like to visit {destination} (yes or no)? ")
        
    if destination_input == "yes":
        print(f"{destination} is a nice place to visit")
        valid_response = "yes"
    else:
        print ("Here is another option")

# Determine restaurant with user input

valid_response = "no"

while valid_response == "no":

    restaurant = random.choice (restaurants)
    restaurant_input = input (f"Would you like to eat at {restaurant}  (yes or no)?  ")

    if restaurant_input == "yes":
        print (f"{restaurant} is a great place to eat")
        valid_response = "yes"
    else:
        print ("Here is another option")

# Determine transportation with user input

valid_response = "no"

while valid_response == "no":

    transport = random.choice (transportation)
    transport_input = input (f"Would you like to get there by {transport}  (yes or no)?   ")

    if transport_input == "yes":
        print (f"{transport} is a fun way to get there")
        valid_response = "yes"
    else:
        print ("Here is another option")

# Determine entertainment with user input

valid_response = "no"

while valid_response == "no":

    entertain = random.choice (entertainment)
    entertain_input = input (f"Would you like to go to {entertain}  (yes or no)?  ")

    if entertain_input == "yes":
        print (f"A {entertain} is a nice experience")
        valid_response = "yes"
    else:
        print ("Here is another option")

# Display the initial random trip

print (f"Visiting {destination}, eating at {restaurant}, traveling by {transport}, and {entertain} makes for a great daytrip" )

# User input on whether satisfied with trip

# Change trip feature

# Display completed trip:

# my_dictionary = {"destinations": (destination), "restaurants": (restaurant),"transportation": (transport), "entertainment": (entertain)}


    
# print (f"Visiting {my_dictionary [destinations], [restaurants]}")
# print (my_dictionary [destination], [restaurant], [transportation], [entertainment])







