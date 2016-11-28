# python exception_from_app_with_multi_middleware.py
# => ブラウザに「raised exception.」
# ターミナルには、
# Middleware3
# Middleware2
# Middleware1
# app
# catch middleware1
# catch middleware2
# catch middleware3
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware1(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        try:
            print("Middleware1")
            return self.app(environ, start_response)
        except Exception:
            print("catch middleware1")
            raise

class Middleware2(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        try:
            print("Middleware2")
            return self.app(environ, start_response)
        except Exception:
            print("catch middleware2")
            raise

class Middleware3(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        try:
            print("Middleware3")
            return self.app(environ, start_response)
        except Exception:
            print("catch middleware3")
            start_response('200 OK', [('Content-Type', 'text/plain')])
            return [b"catch exception middleware3."]


# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        print("app")
        raise Exception
    

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