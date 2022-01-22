let navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const ul = document.querySelector("ul");
let newLi = document.createElement("li");
newLi.textContent = "Logout";

ul.appendChild(newLi);

console.log(ul.firstElementChild.textContent);
console.log(ul.lastChild.textContent);


window.onload = () => {
	const colorsArray = [
		'red',
		'yellow',
		'green'
	];

	const planets = [
	    'Mercury',
	    'Venus',
	    'Earth',
	];

	const section = document.getElementsByTagName('section')[0];
	for (let i = 0; i < planets.length; i++) {
	    const newDiv = document.createElement('div');
	    newDiv.className = 'planet';
	    newDiv.style.backgroundColor = colorsArray[i];
	    section.appendChild(newDiv);
	}
};