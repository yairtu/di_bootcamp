let allBoldItems;

let getBoldItems = () => document.getElementsByTagName("strong");

allBoldItems = getBoldItems();

let highlight = () => {
    for(let i = 0; i < allBoldItems.length; i++) {
        allBoldItems[i].style.color = "blue";
    }
}

highlight();

let return_normal = () => {
    for(let i = 0; i < allBoldItems.length; i++) {
        allBoldItems[i].style.color = null;
    }
}


