def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {'full_name':'Urvisha Bhoi', 'student_ID': 10310981,  'pizza_toppings':['JALAPENOS','MUSHROOM','OLIVES'], 'movies':[{'title':'Koi Mil Gaya..', 'genre':'Sci-Fi'}, {'title':'kgf chapter2','genre':'action'}]}

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title': 'golmaal', 'genre':'comedy'})
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me,about_me['pizza_toppings'])
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])
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
    toppings.append('BACON')
    toppings.append('TOMATOES')
    toppings.sort()
    new_toppings_list = []
    for i in toppings:
        a = i.lower()
        new_toppings_list.append(a)
    about_me['pizza_toppings'] = new_toppings_list
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizaa toppings are:")
    for i in about_me['pizza_toppings']:
        print(f"-{i}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print("I like to watch",end="")
    a = len(about_me['movies'])
    c = 0
    for i in about_me['movies']:
        c = c+1
        if c+1 == a:
            print(i['genre'],end=" and ")
        elif c == a :
            print(f"{i['genre']} movies",end=".")
        else:
            print(" ",end="")
            b = i['genre']
            print(f"{b}, ",end="")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print()
    print("Some of my favourite movies are",end="")
    a = len(movie_list)
    c = 0
    for i in movie_list:
        c = c+1
        if c+1 == a:
            print(f"{i['title'].title()}", end=" and ")
        elif c == a:
            print(f"{i['title'].title()}", end="!")
        else:
            print(f" {i['title'].title()}",end=",")



    return
    
if __name__ == '__main__':
    main()