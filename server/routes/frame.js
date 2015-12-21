var express = require('express');
var router = express.Router();
var mqtt = require('mqtt');

module.exports = function (io) {

    var frame;

    io.on('connection', function (socket) {

        console.log(['mqtt://', process.env.MQTT].join(''));
        var client = mqtt.connect(['mqtt://', process.env.MQTT].join(''));

        client.on('connect', function () {
            client.subscribe('frame');
        });

        client.on('message', function (topic, message) {
            frame = message.toString();
        });

        var recursive = function () {
            setTimeout(function (argument) {
                socket.emit('frame', frame);
                recursive();
            }, 1000 * 0.3);
        };

        recursive();

        socket.on('disconnect', function () {
            client.end();
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
