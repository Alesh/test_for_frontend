import os.path
import tornado.web
import tornado.websocket
from time import time
from random import randint
from tornado.gen import sleep
from tornado.ioloop import IOLoop
from tornado.escape import json_encode


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


class SocketHandler(tornado.websocket.WebSocketHandler):
    started = None

    def open(self, *args, **kwargs):
        IOLoop.current().spawn_callback(self.data_sender)

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        pass

    async def data_sender(self):
        while True:
            x = randint(0, 29)
            y = randint(0, 29)
            n = randint(-999999, 999999) / 100.0
            t = randint(5, 33) / 100.0
            self.write_message(json_encode({'x': x, 'y': y, 'n': n}))
            await sleep(t)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", SocketHandler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"),
       static_path=os.path.join(os.path.dirname(__file__), "static"))
    application.listen(8888)
    IOLoop.current().start()