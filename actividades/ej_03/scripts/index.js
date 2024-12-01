function read_temperature() {
    fetch(`/sensors/ds18b20/read`).then(response => response.json()).then(json => {

        document.querySelector("#valor_temperatura").innerText = json.temperature;
    });
}

function send_setpoint() {
    let setpoint_value = parseInt(document.querySelector("#slider_consigna").value);
    fetch(`/setpoint/set/${valor_consigna}`).then(response => response.json()).then(json => {

        document.querySelector("#buzzer_state").innerText = json.buzzer;
    });
}

// Function to update the setpoint display value
function updateSetpointValue(value) {
    document.getElementById("valor_consigna").innerText = value;
    send_setpoint();
}

setInterval(read_temperature, 500);
