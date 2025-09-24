// Ask the user to choose their favorite color
let color = prompt("Choose your favorite color (red, blue, or green):").toLowerCase();

// Use if/switch to check the input
switch (color) {
    case "red":
        console.log("You picked red");
        break;
    case "blue":
        console.log("You picked blue");
        break;
    case "green":
        console.log("You picked green");
        break;
    default:
        console.log("I don’t know that color");
}

// Print "I like coding" 5 times using a loop
for (let i = 0; i < 5; i++) {
    console.log("I like coding");
}
