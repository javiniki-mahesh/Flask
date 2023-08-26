from flask import Flask, abort, jsonify

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


# returning json format

@app.errorhandler(400)
def bad_request2(error):

    output = {
        'message':'Bad request',
        'status': 400
    }
    return output

@app.errorhandler(401)
def unauthorized1(error):
    output = {
        'message':'401 unauthorized',
        'status': 401
    }
    return output

@app.errorhandler(404)
def page_not_found(error):
    output = {
        'message':'404 page not found',
        'status': 404
    }
    return output

@app.errorhandler(500)
def server_error(error):
    output = {
        'message':'500 Internal Server Error',
        'status': 500
    }
    return output

@app.errorhandler(503)
def server_unavailable(error):
    output = {
        'message':'503 Service Unavailable',
        'status': 503
    }
    return output

if __name__ == '__main__':
    app.run(debug = True)