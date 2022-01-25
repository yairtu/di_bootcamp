let header1 = document.querySelector("h1");
console.log(header1);

let allP = document.querySelector("p");

let pArray = [...document.querySelectorAll("p")];
pArray[pArray.length - 1].remove();



let header2 = document.querySelector("h2");
let changeColor = () => header2.style.backgroundColor = "red";
header2.addEventListener("click", changeColor);

let header3 = document.querySelector("h3");
let hideH3 = () => header3.style.display = "none";
header3.addEventListener("click", hideH3);

let article = document.querySelector("article")
let button = document.createElement("button");
button.style.height = "2em";
button.style.width = "6em";
button.textContent = "click me"
article.appendChild(button);

// let pTextContent = pArray.map(p => p.innerText);
// console.log(pTextContent);
// let b = document.createElement("b");
// console.log(pArray);
// article.appendChild(b);

let boldText = () => pArray.forEach(p => p.style.fontWeight = "900");
button.addEventListener("click", boldText);
let randPix = Math.floor(Math.random() * 100);
console.log(randPix)
let fontSize = () => header1.style.fontSize = `${randPix}px`;

header1.addEventListener("mouseover", fontSize);

let p2 = document.querySelector("#fade");


let fadeout = () => {
    setInterval(hide, 200);
}
let hide = () => {
let fade=document.querySelector("#fade");
opacity =
Number(window.getComputedStyle(fade).getPropertyValue("opacity"))

 if(opacity>0){
        opacity=opacity-0.1;
                p2.style.opacity=opacity
 }
 else{
     clearInterval(intervalID); 
 }
} 


p2.addEventListener("mouseover", fadeout);


