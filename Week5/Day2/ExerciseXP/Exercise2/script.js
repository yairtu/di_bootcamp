console.log(document.querySelector("form"));
console.log(document.querySelector("#fname"));
console.log(document.querySelector("#lname"));
console.log(document.getElementsByName("fname"));
console.log(document.getElementsByName("lname"));

let myform = document.querySelector("form");

function getValues() {
    let ul = document.getElementsByClassName("usersAnswer")[0];
    ul.innerHTML = "";
    let fnameIn = document.getElementById("fname");
    let lnameIn = document.getElementById("lname");
    let inArr = [fnameIn, lnameIn];
    console.log(inArr);
    console.log(ul);

    inArr.forEach(text => {
        let currentLi = document.createElement("li");
        currentLi.textContent = text.value;
        console.log(ul);
        ul.appendChild(currentLi);
    })

    fnameIn.value = "";
    lnameIn.value = "";
}




myform.addEventListener("submit", function (event) {
    event.preventDefault();
    getValues();
})


    // if (inArr[0].length > 0 && inArr[1].length > 0) {
    //     let li = document.createElement("li");
    //     let li2 = document.createElement("li");
    //     li.appendChild(document.createTextNode(`${inArr[0]}`))
    //     li2.appendChild(document.createTextNode(`${inArr[1]}`))
    //     let ul = document.getElementsByClassName("usersAnswer");
    //     ul[0].appendChild(li);
    //     ul[0].appendChild(li2)
    //     console.log(document.querySelectorAll("li"));
    // }


// form.addEventListener("submit", function(event){
//     event.preventDefault();
//     getValues();
// });