let button = document.getElementById("lib-button");
let span = document.getElementById("story");

let noun = document.getElementById("noun");
let adjective = document.getElementById("adjective");
let pName = document.getElementById("person");
let verb = document.getElementById("verb");
let place = document.getElementById("place");

let storyTime = () => {
    // allValues = [noun, adjective, pName, verb, place];
    let allValues = ["noun", "adjective", "person", "verb", "place"]
    .map(str => {console.log(document.getElementById(str)); return document.getElementById(str)});
    for (let i = 0; i < allValues.length; i++) {
        console.log(allValues[i]);
        if (allValues[i].value == "") {
            return alert("no empty strings allowed!");
        }
    }
    span.innerHTML =
        `${pName.value} lived in a ${adjective.value} ${place.value} on the moon. It was very ${adjective.value} and ${pName.value} ${verb.value} very often.`
}

button.addEventListener("click", storyTime);