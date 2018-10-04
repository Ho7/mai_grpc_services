var grpc = require('grpc');
var express = require('express');
var app = express();
var saleProto = grpc.load('sales.proto');

var sale_client = new saleProto.CalculatorSale('127.0.0.1:8001', grpc.credentials.createInsecure());

app.get('/discounts', function (req, res) {
        var cost = getSale(12);
       res.end(JSON.stringify(cost));
});

function printResponse(error, response) {
    if (error)
        console.log('Error: ', error);
    else
        console.log(response);
}

function getSale(cost) {
    sale_client.getSale(cost, function(error, cost) {
        printResponse(error, cost);
    });
    return {'cost': cost}
}

var server = app.listen(8081, function () {


});
