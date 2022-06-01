phone = input("Enter your phone number: ")
digits_map = {
    "1" :  "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = " "

for ch in phone:
    output += digits_map.get(ch, "!") + " "

print(output)