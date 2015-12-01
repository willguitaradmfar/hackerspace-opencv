$(function () {

    var socket = io.connect('http://localhost');

    var heatmap = h337.create({
        container: document.querySelector('body')
    });

    socket.on('heat', function (data) {
        console.log(data);
        heatmap.addData(data);
    });

    socket.on('frame', function (data) {
        $('#frame').attr('src', ['data:image/png;base64,', data].join(''))
    });

    socket.on('counterPoly', function (data) {
        //console.log(data);
    });

});
