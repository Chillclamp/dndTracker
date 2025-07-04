import os
import json


from http.server import HTTPServer, BaseHTTPRequestHandler


class serve(BaseHTTPRequestHandler):
    def do_GET(self):
        # direct to home page
        print(f'cwd - {os.getcwd()}')
        print(self.path)
        if self.path == "/":
            self.path = '/index'
        try:
            # direct to directory
            if self.path[-3:] == 'png' or self.path[-3:] == 'jpg' or self.path[-3:] == 'gif':
                self.path = 'assets' + self.path
            else:
                if self.path[-2:] == 'js':
                    self.path = 'pages/javaScript' + self.path
                elif self.path[-3:] == 'css':
                    self.path = 'pages/style' + self.path
                else:
                    self.path = 'pages/html' + self.path + '.html'

            # direct to other pages
            print(f'here  - {self.path}')
            page = open(self.path, 'rb').read()
            # 200 status code - ok
            
            # header for images - default HTML
            # uses file type
            if self.path[-3:] == 'png':
                self.send_header("Content-type", "image/png")
            elif self.path[-3:] == 'jpg':
                self.send_header("Content-type", "image/jpg")
            elif self.path[-3:] == 'gif':
                self.send_header("Content-type", "image/gif")

            self.send_response(200)

        except FileNotFoundError: # should log?
            # if page does not exist
            page = open('pages/html/notFound.html', 'rb').read()
            # 404 status code - not found
            self.send_response(404)

        except KeyboardInterrupt: # on user shut down
            pass

        except:
            # on major error
            page = open('pages/html/serverError.html', 'rb').read()
            # 500 internal server error
            self.send_response(500)
        
        self.end_headers()
        # send infomation to client
        self.wfile.write(page)

    # def do_POST(self):
    #     error = []
    #     response = []
    #     try:
    #         # length of data
    #         length = int(self.headers.get('content-length'))
    #         # read data as string
    #         data = json.loads(self.rfile.read(length))

    #         if self.path.endswith('/signup'):
    #             printGreen(f'sign up received: {data}')
    #             # handle data
    #             error, response = db.credentials.signup(c, conn, data)
    #             if len(error) > 0:
    #                 printRed(f"sign up error: {error}")


        #     # set data to respond and set as json
        #     response_data = {'error': error, 'response':response}
        #     #printGreen(f'response sent: {response_data}')
        #     json_data = json.dumps(response_data)
        #     page = (bytes(json_data, 'utf-8'))
        #     # Send the header
        #     self.send_response(200)
        #     self.send_header('Content-type', 'application/json')

        # except:
        #     page = open('pages/html/serverError.html', 'rb').read()
        #     self.send_response(500)

        # send response
        self.end_headers()
        self.wfile.write(page)
        


def start_server(host, port):
    # start server
    # printGreen(f"up on: {host}:{port}")
    httpd = HTTPServer((host, port), serve)
    httpd.serve_forever()

    #printRed("server fail")