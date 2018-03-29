import os.path
import tornado.web
import tornado.websocket
from time import time
from random import randint
from tornado.ioloop import IOLoop
from tornado.escape import json_encode


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


class SocketHandler(tornado.websocket.WebSocketHandler):
    started = None

    def send_data(self):
        x = randint(0, 99)
        y = randint(0, 99)
        n = randint(-999999, 999999) / 100.0
        t = randint(0, 33) / 100.0
        self.write_message(json_encode({'x': x, 'y': y, 'n': n}))
        IOLoop().current().add_timeout(time() + t, self.send_data)

    def on_message(self, message):
        if message == "START":
            self.send_data()
        elif message == "STOP":
            if self.started is not None:
                IOLoop().current().remove_timeout(self.started)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", SocketHandler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"),
       static_path=os.path.join(os.path.dirname(__file__), "static"))
    application.listen(8888)
    IOLoop.current().start()