from flask import Flask, request
#request object allows us to access data in request user sent to server
#via python 

import os # ADDED FOR TEMPLATES
import jinja2 # ADDED FOR TEMPLATES

# JOINS LOCATION OF CURRENT LOCATION OF FILE WITH DIRECTORY TO CREATE A NEW DIRECTORY, THE DIRECTORY THAT HOLDS TEMPLATES
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# INITIALIZE JINJA ENGINE, FILE SYSTEM LOADER
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

"""GOAL 1:
Change Index Handler so it returns HTML that consists of
form that user can interact with"""

#Create global variable

form = """


"""

@app.route("/")

def index():
    return form


"""GOAL 2:
Write code to handle our submission to allow a form
to be processed (can customize hello world message)"""

@app.route("/hello", methods=['POST']) #Add methods for post request

def greeting():
    #use get request object by using request.args.get with name
    salutation = request.form['salutation'] #.form[] vs. .args.get()
    user_name = request.form['user_name']
    origin_city = request.form['origin_city']

    greeting = '<h1>Hello, ' + salutation + user_name + '!</h1> <h3>We hope you had a safe trip from ' + origin_city + '!</h3>'

    return greeting


"""
#For POST request, data not exposed in URL:
http://127.0.0.1:5000/hello
"""

app. run()