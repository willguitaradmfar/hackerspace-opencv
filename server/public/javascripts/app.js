$(function () {

    var socket = io.connect();

    var heatmap = h337.create({
        maxOpacity: 0.5,
        minOpacity: 0,
        max: 100,
        min: 0,
        container: document.querySelector('#heat')
    });

    heatmap.setData({
        max: 5,
        data: []
    })

    socket.on('heat', function (data) {

        for (var i in data) {
            data[i] = JSON.parse(data[i]);
            data[i].value = 200;
        }

        heatmap.addData(data)

    });

    socket.on('frame', function (data) {
        $('#frame').attr('src', ['data:image/png;base64,', data].join(''))
    });

    var data = {
        labels: [],
        datasets: [{
            label: "Default",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#000",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: []
        }, {
            label: "Faixa",
            fillColor: "rgba(41,182,197,0.2)",
            strokeColor: "#29b6c5",
            pointColor: "#29b6c5",
            pointStrokeColor: "#29b6c5",
            pointHighlightFill: "#29b6c5",
            pointHighlightStroke: "#29b6c5",
            data: []
        }, {
            label: "ForaDaFaixa",
            fillColor: "rgba(234,155,62,0.2)",
            strokeColor: "#ea9b3e",
            pointColor: "#ea9b3e",
            pointStrokeColor: "#ea9b3e",
            pointHighlightFill: "#ea9b3e",
            pointHighlightStroke: "#ea9b3e",
            data: []
        }]
    };

    var ctx = document.getElementById("myChart").getContext("2d");

    var myLineChart = new Chart(ctx).Line(data);

    var data = {
      Default : 0,
      Faixa : 0,
      ForaDaFaixa : 0
    };

    var ii = 0;

    var addData = function (count) {

        var isNew = false;

        var d = [];

        for (var i in count) {
            if (data[i] != count[i]) {
                isNew = true;
                data[i] = count[i];
            }
        }

        for (var i in data) {
            d.push(data[i]);
        }

        if (d.length == 0 || isNew == false) return;
        var date = new Date().toString().split(' ');
        var t = date[2] + '/' + date[1] + ' ' + date[4];


        myLineChart.addData(d, t);
        ii++;

        if(ii > 20)
          myLineChart.removeData();
    };

    socket.on('counterPoly', function (data) {
        addData(data);
    });

});
