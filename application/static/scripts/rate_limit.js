let label = document.getElementById('time_left');
let outerLabel = document.getElementById('counter_wrap');

var timer = setInterval(() => {
    let clock = label.innerHTML.split(' ');
    let hrs = clock[0];
    let minutes = clock[2];
    let seconds = clock[4];

    console.log(hrs, minutes, seconds);
    seconds -= 1;
    if (seconds < 0){
        seconds = 59;
        minutes -= 1;
    }
    if (minutes < 0){
        minutes = 59;
        hrs -= 1;
    }
    if (hrs < 0){
        outerLabel.innerHTML = '<div id="time_left">Лимит запросов восстановлен. Перезагрузите страницу, чтобы вернуться к приложению :)</div>';
        clearInterval(timer);
    }
    else{
        label.innerHTML = `${hrs} часов ${minutes} минут ${seconds} секунд`;
    }
}, 1000);