from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'

# def allowed_file(filename):
#     # Check if the file extension is allowed
#     ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upimageindex.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('uploaded_file', filename=filename))
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('upresult.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)