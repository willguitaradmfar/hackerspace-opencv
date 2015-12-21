var express = require('express');
var router = express.Router();

// var mongoose = require('./mongo.js')();
//
// var schema = mongoose.Schema({
//     IDD: Number,
//     x: Number,
//     y: Number,
//     value: Number,
//     dtcreate: {
//         type: 'Date',
//         default: Date.now
//     }
// });
//
// var Heat = mongoose.model('Heat', schema);

module.exports = function (io) {

    var heats;

    var mqtt = require('mqtt');

    io.on('connection', function (socket) {

        console.log(['mqtt://', process.env.MQTT].join(''));
        var client = mqtt.connect(['mqtt://', process.env.MQTT].join(''));

        client.on('connect', function () {
            client.subscribe('heats');
        });

        client.on('message', function (topic, message) {
            heats = JSON.parse(message.toString());
        });

        socket.on('disconnect', function () {
            client.end();
        });

        var recursive = function () {
            setTimeout(function (argument) {
                socket.emit('heat', heats);
                for (var i in heats) {
                    // new Heat(JSON.parse(heats[i])).save();
                }
                recursive();
            }, 1000 * 0.3);
        };

        recursive();

    });
    return router;
};
