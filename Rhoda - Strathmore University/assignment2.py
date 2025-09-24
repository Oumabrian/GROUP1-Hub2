# Ask the user to choose their favorite color
color = input("Choose your favorite color (red, blue, or green): ").lower()

# Use if/elif/else to check the input
if color == "red":
    print("You picked red")
elif color == "blue":
    print("You picked blue")
elif color == "green":
    print("You picked green")
else:
    print("I don't know that color")

# Print "I like coding" 5 times using a loop
for i in range(5):
    print("I like coding")
