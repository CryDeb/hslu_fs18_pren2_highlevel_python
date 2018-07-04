from http.server import BaseHTTPRequestHandler
import os
from urllib.parse import urlparse
from urllib.parse import urlsplit
from urllib.parse import parse_qs
import json
from CommunicationServer.Log import LogJSONEncoder


class TrolleyRequestHandler(BaseHTTPRequestHandler):

    on_command_listener = None
    parsed_path = None
    parameters = None
    log_list = None

    #    def __init__(self, onCommandListener):
    #        print "Init TrolleyRequestHandler"
    #        self.onCommandListener = onCommandListener

    def do_GET(self):
        self.parsed_path = urlparse(self.path)

        parameter_list = parse_qs(urlsplit(self.path).query)
        self.parameters = {k.lower(): v[0] for k, v in parameter_list.items()}

        #print(self.parsed_path)
        #print(self.parameters)

        if self.parsed_path.path.lower() == "/api":
            self.response_data()
        else:
            self.response_html()

    def log_message(self, format, *args):
        return

    do_POST = do_GET
    do_PUT = do_GET
    do_DELETE = do_GET

    def response_html(self):
        print("get " + self.parsed_path.path)
        if os.path.isfile("html" + self.parsed_path.path):

            self.send_response(200)

            read_with_utf8 = True

            extension = self.parsed_path.path.split(".")[-1].lower()
            #print("extension: " + extension)
            if extension == "html":
                self.send_header("Content-type", "text/html; charset=utf-8")
            elif extension == "css":
                self.send_header("Content-type", "text/css; charset=utf-8")
            elif extension == "js":
                self.send_header("Content-type", "text/javascript; charset=utf-8")

            elif extension == "gif":
                read_with_utf8 = False
                self.send_header("Content-type", "image/gif")
            elif extension == "png":
                read_with_utf8 = False
                self.send_header("Content-type", "image/png")
            elif extension == "jpeg" or extension == "jpg":
                read_with_utf8 = False
                self.send_header("Content-type", "image/jpeg")
            elif extension == "bmp":
                read_with_utf8 = False
                self.send_header("Content-type", "image/bmp")
            elif extension == "mp3":
                self.send_header("Content-type", "audio/mpeg")
            elif extension == "wav":
                self.send_header("Content-type", "audio/wav")

            else:
                print("else type")
                read_with_utf8 = False
                self.send_header("Content-type", "text/plain; charset=utf-8")

            self.end_headers()

            #print("read: " + str(self.parsed_path.path))
            with open("html" + self.parsed_path.path, 'rb') as f:
                contents = f.read()
                self.wfile.write(contents)

            #html_file = open("html" + self.parsed_path.path)
            #if read_with_utf8:
            #    print("read with utf-8")
            #    self.wfile.write(html_file.read().encode("utf-8"))
            #else:
            #    self.wfile.write(html_file.read())
            #    pass
            #html_file.close()

        else:
            print("not gettet")
            self.response_404()
            return

    def response_400(self):
        self.send_response(400)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>400</h1>Bad request".encode("utf-8"))

    def response_404(self):
        self.send_response(404)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>404</h1>File Not Found".encode("utf-8"))

    def response_data(self):

        dataFile = None

        if "action" in self.parameters:

            if int(self.parameters.get("action")) == 0:

                if "index" in self.parameters:
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header("Content-type", "application/json; charset=utf-8")
                    self.end_headers()


                    index = int(self.parameters.get("index"))
                    if index == -1:
                        self.wfile.write(bytes('{"index":' + str(self.log_list.get_size()-1) + '}', "utf-8"))
                    else:
                        logs = self.log_list.get_logs(index)
                        if logs == None:
                            self.response_400()
                            return
                        self.wfile.write(bytes('{"index":' + str(self.log_list.get_size()-1) + ',"history":' + json.dumps(logs, separators=(',', ':'), cls=LogJSONEncoder) + '}', "utf-8"))

                    return

                else:
                    self.response_400()
                    return

            elif int(self.parameters.get("action")) == 1:
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()

                #print("start command requesthandler")
                error = self.on_command_listener.on_start_command()
                if error == None:
                    self.wfile.write(bytes('{"error":null}', "utf-8"))
                else:
                    self.wfile.write(bytes('{"error":"' + error + '"}', "utf-8"))

            elif int(self.parameters.get("action")) == 2:
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()

                error = self.on_command_listener.on_stop_command()
                if error == None:
                    self.wfile.write(bytes('{"error":null}', "utf-8"))
                else:
                    self.wfile.write(bytes('{"error":"' + error + '"}', "utf-8"))

            else:
                self.response_400()
                return
        else:
            self.response_400()
            return
