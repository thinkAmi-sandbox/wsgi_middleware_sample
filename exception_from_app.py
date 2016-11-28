# python exception_from_app.py
# => ブラウザに「raised exception.」
# ターミナルには、
# Middleware
# app
# raised exception
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        try:
            print("Middleware")
            return self.app(environ, start_response)
        except Exception:
            print("raised exception")
            start_response('200 OK', [('Content-Type', 'text/plain')])
            return [b"raised exception."]


# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        print("app")
        raise Exception
    

# Middlewareを追加
application = WsgiApp()
application = Middleware(application)

if __name__ == "__main__":
    # Middlewareが含まれるWSGIアプリを起動
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()