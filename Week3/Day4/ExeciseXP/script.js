//Exercise 1


let x = 5;
let y = 3;

if (x < y) {
    console.log("x is the biggest number");
} else {
    console.log("y is the biggest number");
}

//Exercise 2
let newDog = "Chihuahua";

console.log(newDog.length);

console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog === "Chihuahua") {
    console.log("I love Chihuahuas, it’s my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}


//Exercise 3
let num = parseInt(prompt("Enter a number"));

if (num % 2 == 0) {
    prompt(`${num} is an even number`);
} else if (num != 0) {
    prompt(`${num} is an odd number`);
} else {
    prompt(`your number is 0`);
}


//Exercise 4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

switch (users.length) {
    case 0:
        console.log("no one is online");
            break;
    case 1:
        console.log(`${users[0]} is online`);
            break;
    case 2:
        console.log(`${users[0]} and ${users[1]} are online`);
            break;
    default:
        console.log(`${users[0]}, ${users[1]} and ${users.length - 2} more are online`);
}