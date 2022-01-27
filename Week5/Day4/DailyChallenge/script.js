let form = document.querySelector("form")
let taskInput = document.querySelector(".taskinput");
let button = document.querySelector(".button");
let listDiv = document.querySelector(".listTasks");
let toDoList = document.querySelector(".todo-list");


let listTasks = [];

let addTask = (event) => {
    event.preventDefault();
    if (taskInput.value.length > 0) {
        listTasks.push(taskInput.value);
        taskInput.value = "";
        console.log(listTasks);
        //create toDoDiv
        let toDoDiv = document.createElement("div");
        toDoDiv.classList.add("todo");
        //create li
        let newToDoItem = document.createElement("li");
        newToDoItem.innerText = listTasks[listTasks.length - 1];
        newToDoItem.classList.add("todo");
        //Check mark button
        let completedButton = document.createElement("input");
        completedButton.type = "checkbox"
        completedButton.classList.add("complete-button");
        //Del button;
        let delButton = document.createElement("button");
        delButton.innerHTML = `<i class="fas fa-times"></i>`;
        delButton.classList.add("complete-button");
        toDoDiv.appendChild(delButton);
        toDoDiv.appendChild(completedButton);
        toDoDiv.appendChild(newToDoItem);
        //append to listDiv
        toDoList.appendChild(toDoDiv);
    } else {
        alert("Please enter a task");
    }

}

let deleteTask = (event) => {
    console.log(event.target);
}

toDoList.addEventListener("onclick", deleteTask)

form.addEventListener("submit", addTask);

// let addTask = (valueToInput) => {
//     if (valueToInput.length > 0) {
//         listTasks.push(valueToInput);
//     } else {
//         alert("Please enter a task");
//     }
//     console.log(listTasks);
//     //create new toDoDiv
//     let toDo = document.createElement("div");
//     toDo.classList = "todo";
//     let newToDoItem = document.createElement("li");
//     newToDoItem.textContent = listTasks[listTasks.size - 1];
// }


// form.addEventListener("submit", (event) => {
//     event.preventDefault();
//     let valueToInput = taskInput.value;
//     addTask(valueToInput);
//     taskInput.value = "";
// })

