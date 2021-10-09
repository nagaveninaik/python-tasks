films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }
while True:
    choice = input("what film whould you like to watch?:").strip().title()

    if choice in films:
        age = int(input("how old are you?:").strip())

        #check the user age

        if age >= films[choice][0]:
            #check enough seats

            num_seats = films[choice][1]

            if num_seats>0:
                print("Enjoy the film!")
                films[choice][1]=films[choice][1]-1
            else:
                print("Sorry,we are sold out1")
        else:
             print("your are too young to see that film!")
    else:
        print("We don't have that film....")
