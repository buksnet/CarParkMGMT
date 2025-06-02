let menu_buttons = document.getElementsByClassName("menu-button-wrap");
let current_url = location.pathname;

switch (current_url) {
    case "/": {
        menu_buttons[0].setAttribute("id", "current-page");
        break;
    }
    case "/vehicles": {
        menu_buttons[1].setAttribute("id", "current-page");
        break;
    }
    case "/routes": {
        menu_buttons[2].setAttribute("id", "current-page");
        break;
    }
    case "/employees": {
        menu_buttons[3].setAttribute("id", "current-page");
        break;
    }
    case "/repairs": {
        menu_buttons[4].setAttribute("id", "current-page");
        break;
    }
    case "/garages": {
        menu_buttons[5].setAttribute("id", "current-page");
        break;
    }
    case "/reports": {
        menu_buttons[6].setAttribute("id", "current-page");
        break;
    }
    case "/settings": {
        menu_buttons[7].setAttribute("id", "current-page");
        break;
    }
}