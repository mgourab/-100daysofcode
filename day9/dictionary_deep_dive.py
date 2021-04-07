programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again."}

# to print the dictionary do this
# print(programming_dictionary["Bug"])

# adding new items to our dictionary

# let's print our dictionary and see the changes
# print(programming_dictionary)

# how to create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary by similar way
# programming_dictionary = {}  # this makes the existing dictionary empty

# edit an item in a dictionary
programming_dictionary["Bug"] = "This has been edited now.."

# how to loop through the dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
