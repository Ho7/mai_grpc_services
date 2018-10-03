var grpc = require('grpc');

var saleProto = grpc.load('sales.proto');

var sale_client = new saleProto.CalculatorSale('127.0.0.1:8001', grpc.credentials.createInsecure());

console.log(saleProto);
console.log(sale_client);

function printResponse(error, response) {
    if (error)
        console.log('Error: ', error);
    else
        console.log(response);
}

function getSale(cost) {
    sale_client.getsale(cost, function(error, cost) {
        printResponse(error, cost);
    });
}
var processName = process.argv.shift();
var scriptName = process.argv.shift();
var command = process.argv.shift();

if (command == 'get_sale'){
    getSale(12);
}