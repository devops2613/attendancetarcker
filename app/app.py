from flask import Flask, jsonify
from sqlalchemy import text
from . import db  # ✅ Correct relative import

from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/health')
def health_check():
    try:
        db.session.execute(text('SELECT 1'))
        return 'OK', 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
