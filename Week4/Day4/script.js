let bottleCountDown = +prompt("Enter a number to begin counting down bottles from :)");
if(isNaN(bottleCountDown)) {
    alert("This is not a number! Refresh the page and try again.");
}
let bottleCount = bottleCountDown;
let bottleCountUp = 1;

for (let i = 1; i <= bottleCount; i++) {
    if (i == 1) {
        console.log(`${bottleCountDown} bottles of beer on the wall\n${bottleCountDown} bottles of beer\ntake ${i} down, pass it around\n${bottleCountDown - 1} bottles of beer on the wall`);
        bottleCountDown--;
    } else if (bottleCountDown == 1) {
        console.log(`${bottleCountDown} bottle of beer on the wall\n${bottleCountDown} bottle of beer\ntake ${i} down, pass them around\n${bottleCountDown - 1} bottles of beer on the wall`);
        bottleCountDown--;
    } else {
        console.log(`${bottleCountDown} bottles of beer on the wall\n${bottleCountDown} bottles of beer\ntake ${i} down, pass them around\n${bottleCountDown - 1} bottles of beer on the wall`);
        bottleCountDown--;
    }
}

