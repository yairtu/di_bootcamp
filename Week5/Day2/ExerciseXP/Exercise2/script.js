console.log(document.querySelector("form"));
console.log(document.querySelector("#fname"));
console.log(document.querySelector("#lname"));
console.log(document.getElementsByName("fname"));
console.log(document.getElementsByName("lname"));

let myform = document.querySelector("form");


function getValues() {
    let fnameIn = document.getElementById("fname").value;
    let lnameIn = document.getElementById("lname").value;
    let inArr = [fnameIn, lnameIn];
    if (inArr[0].length > 0 && inArr[1].length > 0) {
        let li = document.createElement("li");
        let li2 = document.createElement("li");
        li.appendChild(document.createTextNode(`${inArr[0]}`))
        li2.appendChild(document.createTextNode(`${inArr[1]}`))
        let ul = document.getElementsByClassName("usersAnswer");
        ul[0].appendChild(li);
        ul[0].appendChild(li2)
        console.log(document.querySelectorAll("li"));
    }
}





// form.addEventListener("submit", function(event){
//     event.preventDefault();
//     getValues();
// });

myform.addEventListener("submit", function (event) {
    event.preventDefault();
    getValues();
})