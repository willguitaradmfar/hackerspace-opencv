var express = require('express');
var router = express.Router();

var net = require('net');


module.exports = function (io) {

    var counterPoly = {};

    var mqtt = require('mqtt');

    io.on('connection', function (socket) {

        console.log(['mqtt://', process.env.MQTT].join(''));
        var client = mqtt.connect(['mqtt://', process.env.MQTT].join(''));

        client.on('connect', function () {
            client.subscribe('counterPoly');
        });

        client.on('message', function (topic, message) {
            _counterPoly = JSON.parse(message.toString());

            for (var i in _counterPoly) {
                if (counterPoly[i] && _counterPoly[i] == counterPoly[i]) continue;
                socketProtheus(i, _counterPoly[i])
            }

            counterPoly = _counterPoly;
        });

        var socketProtheus = function (name, qtde) {
          // try{
          //   var c = net.connect({
          //       host: '172.16.32.94',
          //       port: 5611
          //   }, function () {
          //       console.log('connected to server!');
          //       c.write([qtde, name+'\r\n'].join(';'));
          //   });
          // }catch(e){
          //   console.error(e);
          //
          // }
        };


        var recursive = function () {
            setTimeout(function (argument) {
                socket.emit('counterPoly', counterPoly);
                recursive();
            }, 1000 * 0.3);
        };

        recursive();

        socket.on('disconnect', function () {
            client.end();
        });

    });
    return router;
};
