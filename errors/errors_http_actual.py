from flask import Flask, abort

app = Flask(__name__)

@app.route('/abort_400')
def abort_400():
    abort(400)

@app.route('/abort_401')
def abort_401():
    abort(401)

@app.route('/abort_404')
def abort_404():
    abort(404)

@app.route('/abort_500')
def abort_500():
    abort(500)

@app.route('/abort_503')
def abort_503():
    abort(503)

# Passing the http error status codes as they occur

@app.errorhandler(400)
def bad_request1(error):
    return '400 Bad Request', 400

@app.errorhandler(401)
def unauthorized1(error):
    return '401 unauthorized', 401

@app.errorhandler(404)
def page_not_found(error):
    return '404 page not found ', 404

@app.errorhandler(500)
def server_error(error):
    return '500 Internal Server Error', 500

@app.errorhandler(503)
def server_unavailable(error):
    return '503 Service Unavailable', 503


if __name__ == '__main__':
    app.run(debug = True)