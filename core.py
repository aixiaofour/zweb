# @Author  : xiaofour
# @Email   : 1325869794@qq.com
# @github  :  baymax-max


from webob import Response, Request

__author__ 'xiaofour'
__version__ = 0.1


class Core:

	"""
	no matter what you request,
	it`s only reponse  `<h1>hello,world</h1>`
	it has lot of thing to do ...

	easy to run it:

		`core = Core()`
    	`core.run()`

	"""

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.make_response(request)
        return response(environ, start_response)

    def make_response(self, request):
        response = Response()
        response.text = '<h1>hello,world</h1>'
        return response

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def run(self, host='127.0.0.1', port=8080):
        from wsgiref.simple_server import make_server
        httpd = make_server(host, port, self)
        print(f'http://{host}:{port}')
        httpd.serve_forever()
