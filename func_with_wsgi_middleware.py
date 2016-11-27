# python func_with_wsgi_middleware.py
# => Middleware
#    WSGI app
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print("Middleware")
        return self.app(environ, start_response)


# WSGI app
def hello_app(environ, start_response):
    print("WSGI app")
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello, middleware."]


# Middlewareの追加
application = Middleware(hello_app)

if __name__ == "__main__":
    # Middlewareが含まれるWSGIアプリを起動
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()