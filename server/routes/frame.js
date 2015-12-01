var express = require('express');
var router = express.Router();
var mqtt = require('mqtt');

module.exports = function (io) {

    var frame;

    // client.on('connect', function () {
    //   client.subscribe('frame');
    // });

    io.on('connection', function (socket) {

        console.log(['mqtt://', process.env.MQTT].join(''));
        var client = mqtt.connect(['mqtt://', process.env.MQTT].join(''));

        client.on('connect', function () {
            client.subscribe('frame');
        });

        client.on('message', function (topic, message) {
            console.log(message.toString().length);

            if(frame)return;

            setTimeout(function () {
              frame = undefined;
            }, 1000 * .5)

            frame = message.toString();

            socket.emit('frame', frame);
        });

    });

    /* GET home page. */
    router.get('/frame', function (req, res, next) {
        // base64Data = frame.replace(/^data:image\/\w*;base64,/,""),
        binaryData = new Buffer(frame, 'base64');

        console.log(binaryData)

        res.writeHead(200, {
            'Content-Type': 'image/png',
            'Content-Length': binaryData.length
        });
        res.end(binaryData);
    });

    return router;

    // body...
};
