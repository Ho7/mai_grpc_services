import time

import grpc
import os

from concurrent import futures
from flask import Flask

import sales_pb2
import sales_pb2_grpc

app = Flask(__name__)


class CalculatorSales(sales_pb2_grpc.CalculatorSaleServicer):

    def GetSale(self, request, context):
        response = sales_pb2.Cost()
        response.value = self._calculate_sale(request.value)
        return response

    @staticmethod
    def _calculate_sale(value):
        return value * 0.5


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    port = 8001

    sales_pb2_grpc.add_CalculatorSaleServicer_to_server(CalculatorSales(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()

    try:
        while True:
            time.sleep(800)
    except KeyboardInterrupt:
        server.stop(0)

    # app.run()
