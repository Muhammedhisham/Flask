from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/image'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return render_template('index.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
