from __future__ import print_function
import grpc

import logging


import client_pb2_grpc
import client_pb2


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = client_pb2_grpc.GreeterStub(channel)
    response = stub.SendData(client_pb2.DataReq(name="karthi007",somethig="xxxxxxxxxxxxyyyyyyyyyyyyzzzz"))
    print(".....................",response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
