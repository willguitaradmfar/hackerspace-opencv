var express = require('express');
var router = express.Router();

var mongoose = require('./mongo.js')();

var schema = mongoose.Schema({
    name: String,
    qtde: Number,
    dtcreate: {
        type: 'Date',
        default: Date.now
    }
});

schema.statics.findByName = function (name) {
    return this.findOne({
        'name': name
    });
};

var Count = mongoose.model('Count', schema);

module.exports = function (io) {

    var counterPoly;

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
                if(counterPoly[i] && _counterPoly[i] == counterPoly[i]) continue;
                findCounter(i, _counterPoly[i])
            }

            counterPoly = _counterPoly;
        });

        var findCounter = function (name, qtde) {
            new Count({
                name: name,
                qtde: qtde
            }).save();
        }

        var recursive = function () {
            setTimeout(function (argument) {
                socket.emit('counterPoly', counterPoly);
                recursive();
            }, 1000 * 0.4);
        };

        recursive();

        socket.on('disconnect', function () {
            client.end();
        });

    });
    return router;
};
