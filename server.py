from concurrent import futures
import logging

import grpc

import user_pb2
import user_pb2_grpc


class keyword(user_pb2_grpc.GreeterServicer):
    def SendData(self,request,context):
        if request.name == "karthi":
            return user_pb2.DataRes(reply='sucess message')
        else:
            return user_pb2.DataRes(reply='username is wrongest')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_GreeterServicer_to_server(keyword(),server)    
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    logging.basicConfig()
    serve()