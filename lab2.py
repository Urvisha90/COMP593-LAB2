def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {'full_name':'Urvisha Bhoi', 'student_ID': 10310981,  'pizza_toppings':['JALAPENOS','MUSHROOM','OLIVES'], 'movies':[{'title':'hera pheri', 'genre':'comedy drama'}, {'title':'kgf chapter2','genre':'action'}]}

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title': 'golmaal', 'genre':'comedy'})
    print_student_name_and_id(about_me)
    return
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    first_name = (full_name.split(' '))[0]
    student_id = about_me['student_ID']
    print(f"My name is {full_name}, but you can call me Ms.{first_name}.")
    print(f"My student ID is {student_id}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()