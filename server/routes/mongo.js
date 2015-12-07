module.exports = function () {
    var mongoose = require('mongoose');

    var connect = function () {
        var url = 'mongodb://'+process.env.MONGO+':27017/';
        console.log("Conectando mongo", url, '.........');
        mongoose.connect(url, {}, function (err) {
            if (err) {
                console.error("ERR: ", err);
                setTimeout(connect, 1000 * 5);
                return;
            }
            console.log('connected Mongo');
        });
    };

    connect();

    return mongoose;

};
