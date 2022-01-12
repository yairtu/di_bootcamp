//Exercise 1
let me = ["my","favorite","color","is","blue"]
console.log(me.join());



//Exercise 2
let str1 = "mix";
let str2 = "pod";

let temp = str1;

str1 = str2.slice(0,2) + str1.slice(2);
str2 = temp.slice(0,2) + str2.slice(2);

let combinedString = str1 + " " + str2;

console.log(combinedString);

//Exercise 3
let num1 = prompt();
let num2 = prompt();

alert(Number(num1) + Number(num2));