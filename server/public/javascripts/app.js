$(function () {

    var socket = io.connect();

    var heatmap = h337.create({
        maxOpacity : 0.5,
        minOpacity : 0,
        max: 100,
        min: 0,
        container: document.querySelector('#heat')
    });

    heatmap.setData({
      max : 5,
      data : []
    })

    socket.on('heat', function (data) {

        for(var i in data){
          data[i] = JSON.parse(data[i]);
          data[i].value = 200;
        }

        heatmap.addData(data)

    });

    socket.on('frame', function (data) {
        $('#frame').attr('src', ['data:image/png;base64,', data].join(''))
    });

    socket.on('counterPoly', function (data) {
        //console.log(data);
    });

});
