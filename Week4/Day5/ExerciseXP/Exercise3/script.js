let mainDiv = document.querySelector("div");
mainDiv.style.backgroundColor = "lightblue";
mainDiv.style.padding = "50px";

let ul = document.getElementsByTagName("ul");
let firstLi = document.getElementsByTagName("li")[0];
let secondLi = document.getElementsByTagName("li")[1];

firstLi.setAttribute("hidden", true);
secondLi.style.border = "5px solid black" 

if(mainDiv.style.backgroundColor == "lightblue") {
    alert(`Hello ${firstLi.textContent} and ${secondLi.textContent}`)
}