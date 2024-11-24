document.addEventListener('DOMContentLoaded', () => {
    const setpointElement = document.getElementById('setpoint');
    const setpointValueElement = document.getElementById('setpoint-value');
    const tempRealElement = document.getElementById('temp-real');
    const buzzerStatusElement = document.getElementById('buzzer-status');

    setpointElement.addEventListener('input', () => {
        setpointValueElement.textContent = setpointElement.value;
    });

    setpointElement.addEventListener('mouseup', updateSetpoint);

    function updateSetpoint() {
        const setpoint = setpointElement.value;
        fetch(`/update_setpoint?value=${setpoint}`)
            .then(response => response.json())
            .then(data => {
                console.log('Setpoint actualizado:', data);
            })
            .catch(error => {
                console.error('Error al actualizar el setpoint:', error);
            });
    }

    function fetchTemperaturaReal() {
        fetch('/get_temp_real')
            .then(response => response.json())
            .then(data => {
                tempRealElement.textContent = data.temp_real;
                buzzerStatusElement.textContent = data.buzzer_status ? 'ON' : 'OFF';
            })
            .catch(error => {
                console.error('Error al obtener la temperatura real:', error);
            });
    }

    setInterval(fetchTemperaturaReal, 5000); // Actualizar cada 5 segundos
});
