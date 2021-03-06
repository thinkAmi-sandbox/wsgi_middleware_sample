# python only_middleware_response_without_app.py
# => middle ware 
# "wsgi app"はprintされない
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print("middle ware")
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b"respond by middleware."]


# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        print("wsgi app")
    

# Middlewareを追加
application = WsgiApp()
applicatoin = Middleware(application)

if __name__ == "__main__":
    # Middlewareが含まれるWSGIアプリを起動
    httpd = make_server('', 8000, applicatoin)
    print("Serving on port 8000...")
    httpd.serve_forever()