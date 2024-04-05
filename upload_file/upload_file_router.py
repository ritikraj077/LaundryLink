
from flask import Flask, request, jsonify, redirect, Blueprint
import os

file_upload = Blueprint('file_upload', __name__)

ALLOWED_EXTENSIONS = ('txt','pdf','png','jpg','jpeg','gif','pdf','png','doc','docx','xls','xlsx','ppt','pptx')

def allowed_file(filename):
    # Check if the file extension is in the allowed extensions 
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@file_upload.route("/upload", methods=['POST'])
def upload_file():
    # Print request files for debugging
    print(request.files)

    if "file" not in request.files:
        return jsonify({"error": "no file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "no selected file"})
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'})
    
    uploaded_file_path = r'C:\Users\rajri\Projects\LaundryLink\upload_file\uploaded_file'
    
    if not os.path.exists(uploaded_file_path):
        os.makedirs(uploaded_file_path)
    
    file.save(os.path.join(uploaded_file_path, file.filename))

    return jsonify({'message': 'File uploaded successfully', "success": True, 'path': uploaded_file_path})

