var clock = document.querySelector("#clock");
var idTime = document.querySelector('#id_time');

var socket = io.connect(location.origin);

socket.on('connect', () => {
    socket.emit('server response', idTime.textContent);
  });

socket.on('client response', (msg) => {
    clock.textContent = msg.data;
});
