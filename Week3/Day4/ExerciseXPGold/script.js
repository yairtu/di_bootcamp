//Exercise 1


let lang = prompt("Which language do you speak?").toLowerCase();

switch (lang) {
    case "french": alert("Bonjour");
        break;
    case "english": alert("Hello");
        break;
    case "hebrew": alert("Shalom");
        break;
    default:
        alert("01110011 01101111 01110010 01110010 01111001");
}


//Exercise 2

let grade = parseInt(prompt("What is your grade?"));

//switch(grade) did not work, why did "lang" work in exercise 1?

switch (true) {
    case (grade > 90): console.log("A");
        break;
    case (grade > 80): console.log("B");
        break;
    case (grade > 69): console.log("C");
        break;
    default: console.log("D");
}


//Exercise 3
//the example given is incorrect:
//"swim" , your program should console.log : "swimming" > ming was added

let verb = prompt("Provide a work that is a verb");

switch (true) {
    case (verb.length > 2 && !verb.includes("ing")): console.log(verb.concat("ing"));
        break;
    case (verb.length > 2 && verb.includes("ing")): console.log(verb.concat("ly"));
        break;
    case (verb.length < 3): console.log(verb);
}