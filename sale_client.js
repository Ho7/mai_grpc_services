var grpc = require('grpc');

var saleProto = grpc.load('sales.proto');

var sale_client = new saleProto.CalculatorSale('127.0.0.1:8001', grpc.credentials.createInsecure());


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
}

console.log(getSale(12));

