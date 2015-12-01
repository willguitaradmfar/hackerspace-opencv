var express = require('express');
var router = express.Router();

module.exports = function (io) {

    var mqtt = require('mqtt');

    io.on('connection', function (socket) {

        console.log(['mqtt://', process.env.MQTT].join(''));
        var client = mqtt.connect(['mqtt://', process.env.MQTT].join(''));

        client.on('connect', function () {
            client.subscribe('counterPoly');
        });

        client.on('message', function (topic, message) {
            console.log(message.toString());
            socket.emit('counterPoly', JSON.parse(message.toString()));
        });

    });
    return router;
};
