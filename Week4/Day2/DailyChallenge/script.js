let strings = prompt("Enter words seperated by commas").split(",");
let longest = "";
let design = "";
let row = "";
let spaces = "";

strings.forEach(string => {
    if (longest.length < string.length) {
        longest = string;
    }
});

let rowTopandBottom = "";

for (let i = 0; i < longest.length + 4; i++) {
    rowTopandBottom += "*";
}

for (let i = 0; i < strings.length; i++) {
    if (strings[i].length <= longest.length) {
        for (let j = 0; j < longest.length - strings[i].length; j++) {
            spaces += " ";
        }
        row += "* " + strings[i] + spaces + " *" + "\n";
        spaces = "";
    }
}

design += rowTopandBottom + "\n" + row + rowTopandBottom;

console.log(design);
