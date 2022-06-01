PROMPT_MSG = input("\n Start to Start the car \n Stop to Sop the car \n Quit to Quit the program\n").upper()


if (PROMPT_MSG) == "START":
    print("CAR Started and you are ready to go")
elif PROMPT_MSG == "STOP":
    print("Car Stopped")
elif PROMPT_MSG == "QUIT":
    print("\n")
else:
    print("Input a valid text")

