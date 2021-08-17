from flask import Flask, render_template, request
import subprocess

from werkzeug.utils import redirect
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/bad_input')
def bad_input():
    return render_template('bad_input.html')

@application.route('/testpost', methods = ['POST'])
def postTesting():
    name = request.form['name']
    if name == "the bird":
        subprocess.run("/usr/bin/systemctl status nginx", shell=True)
        subprocess.run("/usr/bin/sudo /usr/bin/systemctl stop nginx", shell=True)
        subprocess.run("/usr/bin/systemctl status nginx", shell=True)
        print (name)
        return render_template('out.html')
    else:
        return render_template('bad_input.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')