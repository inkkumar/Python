name = input("Enter Name")
print ("[name] lenght(nae)")
print(name)
if len(name) < 3:
    print("Name must be more than 3 characters")

elif len(name) >= 50:
    print("Please enter less than 50 characters")
else:
    print(name, " Your Name looks good")

