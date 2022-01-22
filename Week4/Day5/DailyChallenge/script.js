let makeSolarSystem = () => {
    const planets = [
        "mercury",
        "venus",
        "earth",
        "mars",
        "saturn",
        "jupiter",
        "uranus",
        "neptune",
        "pluto"
    ];

    const colorsArray = [
        "red",
        "yellow",
        "green",
        "blue",
        "white",
        "orange",
        "purple",
        "pink",
        "brown"
    ];

    const section = document.getElementsByTagName("section")[0];
    for (let i = 0; i < planets.length; i++) {
        const newDiv = document.createElement("div");
        newDiv.classList.add("planet", `${planets[i]}`);
        newDiv.style.backgroundColor = colorsArray[i];
        section.appendChild(newDiv);
    }

}

makeSolarSystem();










