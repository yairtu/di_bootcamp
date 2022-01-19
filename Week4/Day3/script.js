let playTheGame = () => {
    let userIn = confirm("Do you want to play?");
    if (userIn == false) {
        return alert("No problem, Goodbye");
    }
    let computerNum = computerNumber();
    
    console.log(computerNum);

    let userNum = userNumber();
    if(isNaN(userNum)) {
        return;
    }
    test(userNum, computerNum);

}

let userNumber = () => {
    let userNum = parseInt(prompt("Enter a number between 0 and 10"));
    //console.log(typeof(userNum)); Always returns number after praseInt so I had to use isNaN to check if its actually a real number
    if (isNaN(userNum)) {
        return alert("Sorry not a number, Goodbye");
    } else if (userNum < 0 || userNum > 10) {
        return alert("Sorry the number is invalid, Goodbye");
    } else {
        return userNum;
    }
}

let computerNumber = () => {
    return Math.floor(Math.random() * 10);
}

let test = (userNum, computerNum) => {
    while (isNaN(userNum)) {
        userNum = parseInt(prompt("Enter a valid number"));
    }
    while (true) {
        if (userNum == computerNum) {
            return alert("WINNER");
        } else if (userNum > computerNum) {
            alert("Your number is is bigger than the computer number");
            userNum = parseInt(prompt("Enter a new number"));
            while (isNaN(userNum)) {
                userNum = parseInt(prompt("Enter a valid number"));
            }
        } else if (userNum < computerNum) {
            alert("Your number is smaller than the computer number");
            userNum = parseInt(prompt("Enter a new number"));
            while (isNaN(userNum)) {
                userNum = parseInt(prompt("Enter a valid number"));
            }
        }
    }
}