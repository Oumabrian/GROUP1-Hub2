#1. Ask the user to input a color
color = input("Enter a color(either red, blue or green): ")

#2. use if/elif/else statements to print a message based on the color they entered
if color == "red":
    print("You picked red.")
elif color == "blue":
    print("You picked blue.")
elif color == "green":
    print("You picked green.")
else:
    print("I dont know that color.")

#3. add a loop that prints "i like coding" 5 times.
for i in range(5):
    print("I like coding")