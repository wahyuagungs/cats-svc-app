from flask import Flask, render_template, jsonify, flash
import os
from utils import get_dbengine, get_uploadfolder
from datetime import timedelta
# from werkzeug.exceptions import HTTPException

# from routes import init_error_handlers

# create the Flask application
app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = get_dbengine()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = get_uploadfolder()

from models.base import db
from controllers.db_controller import db_controller
from controllers.entity_controller import entity_controller
from controllers.module_controller import module_controller

db.init_app(app)
app.register_blueprint(db_controller)
app.register_blueprint(entity_controller)
app.register_blueprint(module_controller)


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    flash(str(e))
    return render_template('500.html'), 500


# @app.errorhandler(Exception)
# def handle_error(e):
#     code = 500
#     if isinstance(e, HTTPException):
#         code = e.code
#     return jsonify({"status": -1, "message": str(e)}), code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
