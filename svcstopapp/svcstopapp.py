from flask import Flask, render_template, request
import os

from werkzeug.utils import redirect
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/error')
def error():
    return render_template('error.html')

@application.route('/testpost', methods = ['POST'])
def postTesting():
    name = request.form['name']
    if name == "the bird":
        os.system("sudo systemctl status nginx")
        print (name)
        return render_template('out.html')
    else:
        return redirect('/error')

if __name__ == "__main__":
    application.run(host='0.0.0.0')