let smallBox = document.querySelector('#smallbox');
let bigBox = document.querySelector('#bigbox')

smallBox.setAttribute('draggable', true);

smallBox.addEventListener("dragstart", (event) => {
    event.target.style.backgroundColor = 'lightpink';
    console.log('drag' + 'X: ' + event.clientX + ' Y: ' + event.clientY)
})

smallBox.addEventListener("dragend", (event) => {
    event.target.style.backgroundColor = 'darkgoldenrod';
    let _x = event.clientX;
    let _y = event.clientY;
    event.target.style.left = _x + 'px';
    event.target.style.top = _y + 'px';
    event.target.style.position = 'absolute';
    console.log('dragend' + 'X: ' + event.clientX + ' Y: ' + event.clientY)
    
})
