from server import *
from flask import jsonify


''' handling HTML errors'''


@app.errorhandler(404)
def handle_404(error):
    alamarapp.logger.info('404 error, bad URL')
    result = {'status': 404, 'message': 'bad URL', 'payload': str(error)}
    return jsonify(result), 404


@app.errorhandler(500)
def handle_500(error):
    alamarapp.logger.error("500 error with the follwing: %s", error)
    return jsonify(TechnicalError('500 error').to_dict()), 500


@app.errorhandler(405)
def handle_405(error):
    alamarapp.logger.info("Method not allowed -- full descreption : %s", error)
    return jsonify({"status": 405, "message": "Method not allowed, read the documentation to check the correct Method"}), 405


@app.errorhandler(400)
def handle_400(error):
    alamarapp.logger.info("error 400 bad request -- full descreption : %s", error)
    return jsonify({"status": 400, "message": "bad request"}), 400
