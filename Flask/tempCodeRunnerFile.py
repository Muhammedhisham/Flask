from flask import Flask, render_template

app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def home():
    return render_template('form.html')

# Define route for the /page route
@app.route('/page')
def next():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
