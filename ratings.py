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
            pair = line.split(':')
            restaurant = pair[0]
            rating = pair[1]
            restaurant_ratings[restaurant] = rating

        return restaurant_ratings


def sort_restaurant(dictionary):
    """takes dictionary, prints it, sorted by keys"""

    sorted_dict = sorted(dictionary.items())
    for item in sorted_dict:
        print "{} is rated at {}.".format(item[0], item[1])


dictionary_to_call = turn_ratings_into_dictionary("scores.txt")
sort_restaurant(dictionary_to_call)    

# rate_restaurant("scores.txt")
