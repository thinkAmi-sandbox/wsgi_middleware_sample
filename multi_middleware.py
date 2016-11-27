# python multi_middleware.py
# => Middleware3
#    Middleware2
#    Middleware1
#    WSGI app
# *追加順とは逆順に動作していることに注意
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware1(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print("Middleware1")
        return self.app(environ, start_response)

class Middleware2(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print("Middleware2")
        return self.app(environ, start_response)

class Middleware3(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print("Middleware3")
        return self.app(environ, start_response)


# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        print("WSGI app")
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b"Hello, class with middleware."]
    

# Middlewareを追加
application = WsgiApp()
application = Middleware1(application)
application = Middleware2(application)
application = Middleware3(application)

if __name__ == "__main__":
    # Middlewareが含まれるWSGIアプリを起動
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()