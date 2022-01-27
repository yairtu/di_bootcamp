let myMove = () => {
    let box = document.getElementById("animate");
    var position = 0;
    
    let frame = () => {
        if(position == 350) {
            clearInterval(id);
        } else {
            position++;
            box.style.top = position + "px";
            box.style.left = position + "px"
        }
    }
    var id = setInterval(frame, 10);
}