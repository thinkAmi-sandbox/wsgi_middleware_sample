# python add_header_middleware.py
# => Middleware
#    WSGI app
#    custom start_response
# また、レスポンスヘッダには、以下が出力されている
# Content-Type: text/plain
# Set-Cookie: hoge=fuga
from wsgiref.simple_server import make_server

# WSGI Middleware
class Middleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        # __call__()メソッドの中に、start_responseをカスタマイズする関数を用意する
        # http://stackoverflow.com/questions/3859097/how-to-add-http-headers-in-wsgi-middleware
        # なお、使う場所よりも前に宣言しておかないと、
        # UnboundLocalError: local variable 'start_response_with_cookie' referenced before assignment
        # また、これは関数なので、第一引数にはselfを設定しないこと
        def start_response_with_cookie(status_code, headers, exc_info=None):
            print("custom start_response")
            headers.append(('Set-Cookie', "hoge=fuga"))
            return start_response(status_code, headers, exc_info)

        print("Middleware")
        return self.app(environ, start_response_with_cookie)


# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        print("WSGI app")
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b"Hello, custom start_response."]
    

# Middlewareを追加
application = WsgiApp()
application = Middleware(application)

if __name__ == "__main__":
    # Middlewareが含まれるWSGIアプリを起動
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()