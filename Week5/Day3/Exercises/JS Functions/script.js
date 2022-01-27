//Ex 1

let bannerContainer = document.querySelector(".banner");
let bannerContent = document.querySelector(".banner_content");
let bannerText = document.querySelector(".banner_text");
let span = document.createElement("span");


let setBanner = () => {
    bannerContainer.style.background = "#009579";
    bannerContainer.style.margin = "0 auto";
    bannerContainer.style.display = "flex";
    bannerContainer.style.alignItems = "center";
    bannerContent.style.padding = "16px";
    bannerContent.style.maxWidth = "1000px";
    bannerContent.style.margin = "0 auto";
    bannerText.style.flexGrow = "1";
    bannerText.style.lineHeight = "1.4";
    bannerText.style.fontFamily = "sans-serif";
    let boldText = document.createTextNode("Reminder!");
    let allText = document.createTextNode(" The sales end in 10sec Get your great deals while supplies last!")
    let boldSpan = bannerText.appendChild(span);
    boldSpan.appendChild(boldText);
    boldSpan.style.fontWeight = "bold";
    bannerText.appendChild(allText);
}

setBanner();

// // setTimeout(setBanner, 5000);
// setBanner();
// bannerText[0].in(`The sales end in sec`);
// // let interval;
// // let num = 5;


let tenSec = 9;

const setText = () => { 
    console.log(tenSec);
    bannerText.innerHTML = `The sales end in ${tenSec}sec`;

    if (tenSec == 0) {
        bannerText.innerHTML = "The sale has ended!"
        clearInterval(time);
    }
    tenSec--;
}

let time = setInterval(setText, 1000);

// let count = 10;
// const timer = () => {
//     console.log(count);
//     count = count -= 1;
// }

// setInterval(timer, 1000);