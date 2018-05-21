from http.server import HTTPServer
from CommunicationServer.TrolleyRequestHandler import TrolleyRequestHandler
from CommunicationServer.LogList import LogList
import threading


class TrolleyCommunicationServer(threading.Thread):

    httpServer = None
    trolleyRequestHandler = None
    log_list = None

    def __init__(self, on_command_listener):
        threading.Thread.__init__(self)

        self.log_list = LogList.get_instance()

        TrolleyRequestHandler.on_command_listener = on_command_listener
        TrolleyRequestHandler.log_list = self.log_list
        self.httpServer = HTTPServer(('', 8080), TrolleyRequestHandler)

    def run(self):
        self.httpServer.serve_forever()

    def log(self, log):
        self.log_list.add_log(log)
        #self.log_list.print_list()
