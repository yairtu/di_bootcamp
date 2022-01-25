let navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const ul = document.querySelector("ul");
let newLi = document.createElement("li");
newLi.textContent = "Logout";

ul.appendChild(newLi);

console.log(ul.firstElementChild.textContent);
console.log(ul.lastChild.textContent);