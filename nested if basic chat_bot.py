
# name = ""
# greet = ""
# thanks = ""


for_wait, for_bye, for_ok, for_where, for_home = "wait", "bye", "ok", "where", "where is your home"

name = input("Hi there! Whats your name?: ")
thanks = input(f"How are you {name} : ")
greet = input(f"Good to see you {name} Enjoy your day.")
go = input("gotta go")



def say_hi():

    if go != for_bye and go != for_wait and go != for_where and go != for_home:
        cont = input(f"Sorry {name} I cant get you! ")

    elif go == for_where:
        my_home = input("To my home")
        if my_home == for_home:
            print("my home is in NewYork, bye! ")

        else:
            print(f"sorry {name}, i have to go, bye! ")
            exit()

    elif go == for_wait and go != for_bye:
        why = input(f"why {name}")
        if why == "i need you":
            sweet_of = input(f"sweet of you {name}")
            exit()
        elif why == "i am bored":
            oh_my = input(f"Oh my dear {name}")
            exit()
        else:
            print("sorry bye")
            exit()

    else:
        print(for_bye)
        exit()

say_hi()
