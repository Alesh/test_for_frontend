var ws = new WebSocket("ws://localhost:8888/websocket");

ws.onmessage = function (evt) {
    console.log(evt.data);
};