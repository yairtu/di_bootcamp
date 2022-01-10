//Exercise 1


let favFood = "sous vide cowboy steak";
let favMeal = "dinner";

console.log("I eat " + favFood + " at every " + favMeal);


//Exercise 2 part 1
let watchedSeries = ["black mirror", "money heist", "the big bang theory"];
let watchedSeriesLength = watchedSeries.length;

let myWatchedSeries = watchedSeries[0] + ", " + watchedSeries[1] + ", " + watchedSeries[2];

console.log("I watched 3 series : " + myWatchedSeries);

//Exercise 2 part 2
watchedSeries.pop();
watchedSeries.push("friends");
watchedSeries.push("silicon valley");
watchedSeries.unshift("better call saul");
watchedSeries.splice(1, 1);
console.log(watchedSeries[1][2]);
console.log(watchedSeries);

//Exercise 3
let cel = 20;
let f = (cel / 5 * 9) + 32;

console.log(cel + "°C is " + f + "°F");

//Exercise 4
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55 because 34+21 = 55
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: 23 because a is redefined and given the value 2 so 2 + 21 = 23
// Actual: 23

//What is the value of c? 
//prediction: Undefined
//Actual: Undefined

//Analyse the code below, what will be the outcome?
console.log(3 + 4 + '5');

//prediction:75 because 3+4 are integers and '5' is a string in this case, and they 
//are concatenated

//Actual: 75



console.log(typeof(15));
// Prediction: integer
// Actual: number


console.log(typeof(5.5));
// Prediction: double
// Actual: number

console.log(typeof(NaN));
// Prediction: NaN
// Actual: number, if it stands for "Not a Number", Why is number returned???


console.log(typeof("hello"));
// Prediction: string
// Actual: string.


console.log(typeof(true));
// Prediction: boolean
// Actual: boolean


console.log(typeof(1 != 2));
// Prediction: boolean
// Actual: boolean


console.log("hamburger" + "s");
// Prediction: hamburgers
// Actual: hamburgers


console.log("hamburgers" - "s");
// Prediction: error
// Actual: NaN


console.log("1" + "3");
// Prediction: 13
// Actual: 13


console.log("1" - "3");
// Prediction: NaN
// Actual: -2, 1 and 3 are both strings in this case, why does it return an integer?


console.log("johnny" + 5);
// Prediction: johnny5
// Actual: johnny5


console.log("johnny" - 5);
// Prediction: NaN
// Actual: NaN


console.log(99 * "hello");
// Prediction: NaN
// Actual: NaN


console.log(1 != 1);
// Prediction: false
// Actual: false


console.log(1 == "1");
// Prediction: false
// Actual: true


console.log(1 === "1");
// Prediction: false
// Actual: false


//Exercise 6

console.log(5 + "34");
// Prediction: 534
// Actual: 534


console.log(5 - "4");
// Prediction: NaN
// Actual: 1, got me again...


console.log(10%5);
// Prediction: 0, there is no remainder when 5 goes into 10 twice
// Actual: 0


console.log(5%10);
// Prediction: 5 
// Actual: 5


console.log("Java" + "Script");
// Prediction: JavaScript
// Actual:JavaScript


console.log(" " + " ");
// Prediction: "  " (with no "")
// Actual: "  "


console.log(" " + 0);
// Prediction: " 0"
// Actual: " 0"


console.log(true + true);
// Prediction: true
// Actual: 2


console.log(true + false);
// Prediction: 1 because true = 1 and false = 0
// Actual: 1


console.log(false + true);
// Prediction: 1 because true = 1 and false = 0
// Actual: 1


console.log(false - true);
// Prediction: -1
// Actual: -1


console.log(!true);
// Prediction: false
// Actual: false


console.log(3 - 4);
// Prediction: -1
// Actual: -1

console.log("Bob" - "bill");
// Prediction: NaN
// Actual: NaN