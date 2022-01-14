//Exercise 1
//Part 1

let people = ["Greg", "Mary", "Devon", "James"];

people.splice(0, 1);
people.splice(-1, 1, "Jason");
people.push("Yair");

console.log(people)
console.log(people.indexOf("Mary"));

people.slice(1, 3);

people.indexOf("foo"); // returns -1 because foo is not in the array, so it is undefined.

let last = people.length - 1;

//Exercise 1
//Part 2

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}

for (let i = 0; i < people.length; i++) {
    if (people[i] == "Jason") {
        console.log(people[i]);
        break;
    }
    console.log(people[i]);
}


//Exercise 2
let colors = ["blue", "green", "yellow", "red", "purple"];
let suffix = ["st", "nd", "rd", "th"]

for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i + 1} choice is ${colors[i]}`);
}

console.log("")

for (let i = 0; i < colors.length; i++) {

    if (i > 3) {
        console.log(`My ${i + 1}${suffix[3]} choice is ${colors[i]}`)
        continue;
    }

    console.log(`My ${i + 1}${suffix[i]} choice is ${colors[i]}`)
}

// Exercise 3

while (true) {
    let num = parseInt(prompt("Enter a number"));
    if (num >= 10) {
        break;
    }
}

// Exercise 4



let objct = {
    1: "One",
    2: "Two",
    3: "Three",
    Four: 4,
    5: "Five"
}


let building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors);
console.log(`first floor # of apartments: ${building.numberOfAptByFloor.firstFloor}`);
console.log(`third floor # of apartments: ${building.numberOfAptByFloor.thirdFloor}`)


let secondTentant = building.nameOfTenants[1]
let numRoomsAndRentSecondTenant = building.numberOfRoomsAndRent[secondTentant];
let numRoomsSecondTenant = numRoomsAndRentSecondTenant[0];

//if you just try to use the second tenant without toLowerCase() it wont work cause the property is dan not Dan
console.log(`${building.nameOfTenants[1]} has ${building.numberOfRoomsAndRent[secondTentant.toLowerCase()][0]} rooms`);

//another way is to split it up:
// let secondTentant = building.nameOfTenants[1].toLowerCase()
// let numRoomsAndRentSecondTenant = building.numberOfRoomsAndRent[secondTentant];
// let numRoomsSecondTenant = numRoomsAndRentSecondTenant[0];



//Exercise 5
let family = {
    mom: "Lucy",
    dad: "Joe",
    firstChild: "dave"
}

for (const key in family) {
    console.log(key);
}

for (const key in family) {
    console.log(family[key]);
}

// Exercise 6
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}

let sent = "";

for (const key in details) {

    sent += `${key} ${details[key]} `
}

console.log(sent);

// Exercise 7
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names = names.sort();
let secretName = "";

for (let i = 0; i < names.length; i++) {
    secretName += names[i][0];
}

console.log(secretName);