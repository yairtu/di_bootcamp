// Exercise 1

let bob = {
    FullName: "Bob",
    Weight: 27,
    Height: 180,
    BMI: function () {
        return this.Weight / this.Height / this.Height * 10000;
    }
}

let joe = {
    FullName: "Joe",
    Weight: 28,
    Height: 170,
    BMI: function () {
        return this.Weight / this.Height / this.Height * 10000;
    }
}

// if else statement

// if (bob.BMI() < joe.BMI()) {
//     console.log(joe.FullName);
// } else if (joe.BMI() < bob.BMI()) {
//     console.log(bob.FullName);
// } else {
//     console.log("Oops their BMI is the same")
// }

// switch statement with same result
switch (bob.BMI() < joe.BMI()) {
    case true: console.log(joe.FullName);  
        break;
    case false: console.log(bob.FullName);
        break;
    default: "Oops they have the same BMI";
        break;
}

// Exercise 2

let grades = [50, 55, 60]

function findAverage (gradesList) {
    let sum = 0;
    for(let i = 0; i < gradesList.length; i++) {
        sum += gradesList[i];
    }
    return sum/gradesList.length;
}

console.log(findAverage(grades));

function passOrFail(num) {
    if (num < 65) {
        console.log("Sorry, you failed. You must repeat the course.");
    } else {
        console.log("Hooray you passed!");
    }
}

passOrFail(findAverage(grades));

