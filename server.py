import os.path
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], template_path=os.path.join(os.path.dirname(__file__), "templates"),
       static_path=os.path.join(os.path.dirname(__file__), "static"))
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()