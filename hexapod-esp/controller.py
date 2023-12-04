from microdot_asyncio import Microdot
from microdot_asyncio import send_file

def start():
    app = Microdot()

    @app.route('/')
    def index(request):
        return send_file("/static/index.html")
    
    @app.route('/static/<path:path>')
    def static(request, path):
        if '..' in path:
            # directory traversal is not allowed
            return 'Not found', 404
        return send_file('static/' + path, max_age=86400)


    app.run(port=80)
