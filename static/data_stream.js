var ws = new WebSocket("ws://localhost:8000/ws/data");

ws.onmessage = function(event) {
    var data = JSON.parse(event.data);
    document.getElementById('temperature').textContent = data.temperature;
    document.getElementById('humidity').textContent = data.humidity;
};