attempts = 0
input_txt = ""
while input_txt != "quit":
    input_txt = input(">")
    if (input_txt) == "start":
        print("CAR Started and you are ready to go")
    elif input_txt == "stop":
        print("Car Stopped")
    elif input_txt == "quit":
        print("thanks for using")
    elif input_txt == "help":
        print ("""
           Start to Start the CAR
           Stop to Stop th eCAR
           QUIT to exit the program 
        """)
    else:
        print("Sorry , i don't understand your message ")
        attempts = attempts + 1
        if((attempts) > 3 ):
            print("type help to see the commands")
            if attempts > 5:
                print("Quitting due to incoorect entries")
                break

