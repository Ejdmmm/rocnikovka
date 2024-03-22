from microdot_asyncio import Microdot
from microdot_asyncio import send_file
import wave as servowave

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
    
    @app.route('/wave')
    def wave(request):
        servowave.wave()
        return send_file("/static/index.html")

    app.run(port=80)
