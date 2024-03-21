from flask import Flask, render_template,request

app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def home():
    return render_template('form.html')

# Define route for the /page route
@app.route('/table',methods=['POST'])
def next():
    name=request.form['name']
    mail=request.form['email']
    age=request.form['age']
    return render_template('table.html',name=name,email=mail,age=age)
@app.route('/image')
def image():
    return render_template('image.html')
if __name__ == '__main__':
    app.run(debug=True)
