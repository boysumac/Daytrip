greeting = "Hi there"

print(greeting)

import random

# list of places

places = ['Milwaukee', 'Door County', 'Madison','Crivitz']          

place = random.choice (places)

print(place)
valid_response = "no"

while valid_response == "no":

    location = input("Would you like to go to?")

    if location == "yes":
        print("This is a good place to go")
        valid_response = "yes"
    else:
        print ("another choice needed")



#list of restaurants


#list of activities

# Input your daytrip requests
