
let stars = "*";

for (let i = 0; i < 6; i++) {
    console.log(stars);
    stars += "*";
}


//same challenge nested loop

let n = 6;
let star = "";

for (let i = 1; i <= 6; i++) {
    for (let ind = 0; ind < i; ind++) {
        star += "*";
    }
    star += "\n";
}

console.log(star);