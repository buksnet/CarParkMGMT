let fields = document.querySelectorAll(".row-wrap");

fields.forEach(field => {
    field.addEventListener("click", function (event) {
        let previously_selected = document.getElementById("row-selected");
        if (previously_selected) previously_selected.removeAttribute("id");
        field.setAttribute("id", "row-selected");
    })
});