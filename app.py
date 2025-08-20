
from flask import Flask, request, jsonify, send_file
from database import get_db_connection
from crypto_utils import encrypt_file, decrypt_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/register', methods=['POST'])
def register():
    return jsonify({"message": "Register API placeholder"})

@app.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login API placeholder"})

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    encrypt_file(path)
    return jsonify({"message": f"File {filename} uploaded and encrypted."})

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(path):
        return jsonify({"error": "File not found"}), 404
    decrypt_file(path)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
