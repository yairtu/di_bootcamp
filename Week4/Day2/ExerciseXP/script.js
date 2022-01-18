// //Exercise 1
// //Part 1
// let infoAboutMe = () => console.log("Hello my name is Yair and I am learning to code at Developers Institute!");

// infoAboutMe();

// // Part 2
// let infoAboutPerson = (personName, personAge, personFavoriteColor) =>
//     console.log(`Your name is ${personName}, your are ${personAge} years old, your favorite color is ${personFavoriteColor}`);

// infoAboutPerson("David", 45, "blue");
// infoAboutPerson("Josh", 12, "yellow");

// // Exercise 2

// let calculateTip = () => {
//     let bill = parseInt(prompt("What is the total amount of the bill?"));

//     switch (true) {
//         case (bill > 0 && bill < 50): console.log(bill + (bill * 0.2));
//             break;
//         case (bill >= 50 && bill < 200): console.log(bill + (bill * 0.15));
//             break;
//         case (bill >= 200): console.log(bill + (bill * 0.1));
//             break;
//         default: console.log("Invalid amount")
//             break;
//     }
// }

// calculateTip();


// // Exercise 3

// let isDivisable = () => {
//     let sum = 0;
//     let nums = [];
//     for (let i = 0; i < 501; i++) {
//         if (i % 23 == 0) {
//             sum += i;
//             nums.push(i);
//         }
//     }
//     console.log(`Outcome: ${nums.join(" ")}`);
//     console.log(`Sum: ${sum}`);
// }

// isDivisable();

// Bonus
// let isDivisableBy = (num) => {
//     let sum = 0;
//     let nums = [];
//     for (let i = 0; i < 501; i++) {
//         if (i % num == 0) {
//             sum += i;
//             nums.push(i);
//         }
//     }
//     console.log(`Outcome: ${nums.join(" ")}`);
//     console.log(`Sum: ${sum}`);
// }

// isDivisableBy(5);

// // Exercise 4

// let stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// }

// let prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// }

// let shoppingList = ["banana", "orange", "apple"];

// console.log(stock[shoppingList[1]])

// let myBill = () => {
//     let sum = 0;
//     shoppingList.forEach(element => {
//         if (stock[element] > 0) {
//             sum += prices[element];
//             stock[element] = stock[element] - 1;

//         }
//     });
//     console.log(sum);
// }

// myBill();

// Exercise 5

let changeEnough = (itemPrice, amountOfChange) => {
    let sum = 0;
    amountOfChange.forEach((element, i) => {
        if (i == 0) {
            sum += element * 0.25;
        } else if (i == 1) {
            sum += element * 0.10;
        } else if (i == 2) {
            sum += element * 0.05;
        } else {
            sum += element * 0.01;
        }
    });
    if (sum < itemPrice) {
        return false;
    }
    return true;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));


// // Exercise 6
// // Part 1
// let hotelCost = () => {

//     let nights = 0;

//     while (true) {
//         nights = parseInt(prompt("How many nights would you like to stay in the hotel?"));

//         if (typeof (nights) == 'number') {
//             break;
//         }
//     }
//     let totalCost = nights * 140;

//     return totalCost;
// }


// //Part 2

// let planeRideCost = () => {
//     let destination = "";
//     let price = 0;

//     while (true) {
//         //prompt automatically converts everything into a string so even if you input
//         //a number it will still register as a string. What would be the solution to that?
//         destination = prompt("What is your destination?");
//         if (destination.length > 0 && typeof (destination) == 'string') {
//             console.log(destination)
//             break;
//         }
//     }

//     switch (destination.toLowerCase()) {
//         case "london":
//             price = 183;
//             break;
//         case "paris":
//             price = 220;
//             break;
//         default:
//             price = 300;
//             break;
//     }
//     return price;
// }


// //Part 3

// let rentalCarCost = () => {
//     let rentalDays = 0;

//     while (true) {
//         rentalDays = parseInt(prompt("How many days would you like to rent the car for?"));
//         if (typeof (rentalDays) == 'number') {
//             break;
//         }
//     }

//     if (rentalDays > 10) {
//         return (rentalDays * 40) * 0.95;
//     } else {
//         return rentalDays * 40;
//     }
// }


// //Part 4
// let totalVacationCost = () => {
//     return hotelCost() + planeRideCost() + rentalCarCost();
// }

// console.log(totalVacationCost());