var ws = new WebSocket("ws://localhost:8888/websocket");

ws.onopen = function() {
   ws.send("START");
};

ws.onmessage = function (evt) {
    console.log(evt.data);
};