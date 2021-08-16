from flask import Flask, render_template, request
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/testpost', methods = ['POST'])
def postTesting():
    name = request.form['name']
    print (name)
    return render_template('out.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')