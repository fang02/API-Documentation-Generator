from flask import Flask, request, jsonify
from flask_cors import CORS
import ast
import os
import zipfile
import shutil

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_code():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    upload_dir = 'uploads'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    zip_path = os.path.join(upload_dir, file.filename)
    file.save(zip_path)

    extraction_path = os.path.join(upload_dir, 'extracted_code')
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
    except zipfile.BadZipFile:
        return jsonify({"error": "Invalid zip file"}), 400

    documentation_data = {}
    for root, dirs, files in os.walk(extraction_path):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                documentation_data[file_name] = process_python_file(file_path)

    # Clean up temporary files and folders
    os.remove(zip_path)
    shutil.rmtree(extraction_path)

    return jsonify(documentation_data)

def process_python_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename=file_path)

    doc_data = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            name = node.name
            docstring = ast.getdoc(node)
            params = []
            if isinstance(node, ast.FunctionDef):
                for arg in node.args.args:
                    params.append(arg.arg)

            doc_data.append({
                'name': name,
                'type': 'function' if isinstance(node, ast.FunctionDef) else 'class',
                'parameters': params,
                'docstring': docstring
            })
    return doc_data

if __name__ == '__main__':
    app.run(debug=True)