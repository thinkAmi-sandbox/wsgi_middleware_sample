# python middleware_response.py
# ・クエリ文字列が無い場合、画面にrespond by app.と表示
# ・クエリ文字列がある場合、画面にrespond by middleware.と表示
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        if environ['QUERY_STRING']:
            start_response('200 OK', [('Content-Type', 'text/plain')])
            return [b"respond by middleware."]
        return self.app(environ, start_response)

# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b"respond by app."]
    

# Middlewareを追加
application = WsgiApp()
application = Middleware(application)

if __name__ == "__main__":
    # Middlewareが含まれるWSGIアプリを起動
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()