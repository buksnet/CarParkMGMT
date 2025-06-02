let vehicles = document.querySelectorAll(".row-wrap");

vehicles.forEach(vehicle => {
    console.log(vehicle);
    vehicle.addEventListener("click", function (event) {
        let previously_selected = document.getElementById("row-selected");
        if (previously_selected) previously_selected.removeAttribute("id");
        vehicle.setAttribute("id", "row-selected");
    })
});