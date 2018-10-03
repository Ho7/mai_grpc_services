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


class SalesServer:
    _max_workers = 5
    _default_port = 8001

    def run_server(self):
        server = self._get_grpc_server()
        server.start()

    def _get_grpc_server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=self._max_workers))
        port = self.get_port()

        sales_pb2_grpc.add_CalculatorSaleServicer_to_server(CalculatorSales(), server)
        server.add_insecure_port(f'[::]:{port}')

        return server

    def get_port(self):
        return int(os.getenv('LISTEN_PORT', self._default_port))


if __name__ == "__main__":
    SalesServer().run_server()
    while True:
        time.sleep(80000)
    # app.run()
