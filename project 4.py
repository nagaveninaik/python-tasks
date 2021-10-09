known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! My name is travis")
    name=input("What is your name?:").strip().capitalize()

    if name in known_users:
        print("hello{}!".format(name))
        remove=input("Whould you like to be removed from the system(y/n)?:").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print(" No problem,i didn't want you to leave anyway!")

    else:
        print("Hmmm Idon't think i have meet you yet{}".formet(name))
        add_me = input("Whould you like to be added to the system (y/n)?:").strip().lower()
        if add_me =="y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries,see you arround!")
        
