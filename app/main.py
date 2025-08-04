from flask import Flask, request, jsonify
from models import db, Attendance
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    if not data or 'name' not in data or 'status' not in data:
        return jsonify({"error": "Missing 'name' or 'status' in request"}), 400
    record = Attendance(name=data['name'], status=data['status'])
    db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Attendance marked"}), 201

@app.route('/attendance', methods=['GET'])
def get_attendance():
    records = Attendance.query.all()
    return jsonify([{"name": r.name, "status": r.status} for r in records])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)

@app.route('/attendance/check')
def check():
    print("API /attendance/check hit")
    return jsonify({"status": "success"}), 200

