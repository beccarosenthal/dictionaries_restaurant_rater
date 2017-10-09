"""Restaurant rating lister."""

# Your job is to write a program named ratings.py that:

# Reads the ratings in from the file
# Stores them in a dictionary, and then
# Spits out the ratings in alphabetical order by restaurant
# put your code here


def turn_ratings_into_dictionary(file_name):
    """takes file name, returns sorted dict with restaurant:rating pairs"""

    with open(file_name) as the_file:
        
        restaurant_ratings = {}

        for line in the_file:
            line = line.rstrip()
            restaurant, rating = line.split(':')
            restaurant = restaurant.title()
            restaurant_ratings[restaurant] = rating

        return restaurant_ratings


def print_sorted_restaurants(dictionary):
    """takes dictionary, prints it, sorted by keys"""

    sorted_dict = sorted(dictionary.items())
    for restaurant, rating in sorted_dict: #restaurant/rating unpack tuple
        print "{restaurant} is rated at {rating}.".format(restaurant=restaurant, 
            rating=rating)

# rate_restaurant("scores.txt")

# The program should:

# Prompt the user for a restaurant name
# Prompt the user for a restaurant score.
# Store the new restaurant/rating in the dictionary.
# Print all of the ratings in alphabetical order (including the new one, of course).

def add_restaurant_and_rating_to_dict(dictionary):
    """generate user input for new restaurant/rating; add to dictionary, returns it"""

    while True:
        
        keys_to_check_against = [key.lower() for key in dictionary.keys()]    
        # import pdb; pdb.set_trace() #pauses program right here
        # so you can troubleshoot and call variables/fns at this point
        rest_name = raw_input("Which restaurant would you like to add? > ").title()
        if rest_name.lower() in keys_to_check_against:
            print "{} is already in the dictionary, and its rating is {}.".format(
                rest_name, dictionary[rest_name])
            return dictionary
        
        rating = validate_rating()
        break

    dictionary[rest_name] = rating
    return dictionary      


def validate_rating():
    """gets user generated rating between 1-5, returns it"""

    while True:
        
        rating = raw_input("What is its rating? (1-5, with 5 as the best) > ")
        try:
            rating = float(rating)
        except:
            print "Dude...learn to read..."
            continue
        if not(0.0 < rating <= 5.0):
            print "Dude...learn to read..."
            continue
        return rating


def REPL(file_name):
    """runs the things"""
    ratings_dict = turn_ratings_into_dictionary(file_name)
    
    while True:

        ratings_dict = add_restaurant_and_rating_to_dict(ratings_dict) 
        print_sorted_restaurants(ratings_dict)    
        continue_or_no = raw_input("Want to add a new restaurant? (Y/N) > ")
        if continue_or_no.lower() == "n":
            print "Have a nice life!"
            break



REPL("scores.txt")
