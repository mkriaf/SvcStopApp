from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testpost', methods = ['POST'])
def postTesting():
    name = request.form['name']
    print (name)
    return render_template('out.html')
