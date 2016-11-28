# python exception_from_middleware.py
# => ブラウザに「A server error occurred.  Please contact the administrator.」
# ターミナルには
# Middleware
# Traceback (most recent call last):
# ...
#   File "exception_from_middleware.py", line 12, in __call__
#     raise Exception
# Exception
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print("Middleware")
        raise Exception


# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        try:
            print("WSGI app")
            start_response('200 OK', [('Content-Type', 'text/plain')])
            return [b"Hello, class with middleware."]
        except:
            print("exception")
    

# Middlewareを追加
application = WsgiApp()
application = Middleware(application)

if __name__ == "__main__":
    # Middlewareが含まれるWSGIアプリを起動
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()