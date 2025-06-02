var config = {
    responsive: true,
    displaylogo: false
}
async function fetchVehiclesCounts() {
    const response = await fetch('/api/index/get-vehicle-count', {
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        }
    });
    const obj = await response.json()
    return obj;
}

async function fetchWorkersCounts() {
    const response = await fetch('/api/index/get-worker-count', {
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    });
    const obj = await response.json();
    return obj;
}

async function fetchDriversCounts() {
    const response = await fetch('/api/index/get-driver-count', {
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        }
    });
    const obj = await response.json();
    return obj;
}



fetchVehiclesCounts().then(data => {
    var vehicle_data = [
        {
            domain: { x: [0, 1], y: [0, 1] },
            value: data.active,
            title: { text: "Техника" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                bordercolor: "#C8D0D9",
                bar: { color: "#C8D0D9" },
                axis: { tickcolor: "#C8D0D9", range: [0, Math.max(data.total_count, 1)] }
            }
        }
    ];
    var vehicle_layout = {
        margin: { t: 0, b: 0 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#C8D0D9' }
    };

    Plotly.newPlot('car-graph', vehicle_data, vehicle_layout, config);

});

fetchWorkersCounts().then(data => {
    var workers_data = [
        {
            domain: { x: [0, 1], y: [0, 1] },
            value: data.active,
            title: { text: "Сотрудники" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                bordercolor: 'black',
                bar: { color: 'black' },
                axis: { tickcolor: 'black', range: [0, Math.max(data.total_count, 1)] }
            }
        }
    ]

    var workers_layout = {
        margin: { t: 0, b: 0 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#11447C' }
    }
    Plotly.newPlot('worker-graph', workers_data, workers_layout, config);

});


fetchDriversCounts().then(data => {
    var drivers_data = [
        {
            domain: { x: [0, 1], y: [0, 1] },
            value: data.active,
            title: { text: "Водители" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                bordercolor: "#C8D0D9",
                bar: { color: "#C8D0D9" },
                axis: { tickcolor: "#C8D0D9", range: [0, Math.max(data.total_count, 1)] }
            }
        }
    ];

    var drivers_layout = {
        margin: { t: 0, b: 0 },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#C8D0D9' }
    };

    Plotly.newPlot('driver-graph', drivers_data, drivers_layout, config);

});
