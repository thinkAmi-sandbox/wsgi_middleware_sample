# 素のWSGIアプリ
# middlewareの作り方は以下を参照
# http://gihyo.jp/dev/feature/01/wsgi/0003

# python func_without_wsgi_middleware.py

from wsgiref.simple_server import make_server

def hello_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello, world."]

if __name__ == "__main__":
    httpd = make_server('', 8000, hello_app)
    print("Serving on port 8000...")
    httpd.serve_forever()