from flask import Flask, request
#request object allows us to access data in request user sent to server
#via python 
import cgi
import os # ADDED FOR TEMPLATES
import jinja2 # ADDED FOR TEMPLATES

# JOINS LOCATION OF CURRENT LOCATION OF FILE WITH DIRECTORY TO CREATE A NEW DIRECTORY (THE DIRECTORY THAT HOLDS TEMPLATES)
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# INITIALIZE JINJA ENGINE, FILE SYSTEM LOADER
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True) #APPLIES HTML ESCAPE TO ALL

app = Flask(__name__)
app.config['DEBUG'] = True

"""GOAL 1:
Change Index Handler so it returns HTML that consists of
form that user can interact with"""

#Create global variable



@app.route("/")

def index():
    # USE JINJA ENGINE TO RENDER THE FORM INSTEAD OF SIMPLY RETURNING THE FORM DIRECTLY
    template = jinja_env.get_template('hello_form.html') # TELLS JINJA TO GO FIND TEMPLATE hello_form.html FOR ME
    return template.render() # RENDERS TEMPLATE INTO A STRING VS. JUST RETURNING form


"""GOAL 2:
Write code to handle our submission to allow a form
to be processed (can customize hello world message)"""

@app.route("/hello", methods=['POST']) #Add methods for post request

def greeting():
    #use get request object by using request.args.get with name
    salutation = request.form['salutation'] #.form[] vs. .args.get()
    user_name = request.form['user_name']
    my_city = request.form['origin_city']

    template = jinja_env.get_template('hello_greeting.html')

    return template.render(salutation=salutation, user_name=user_name, origin_city=my_city)


"""
#For POST request, data not exposed in URL:
http://127.0.0.1:5000/hello
"""

app. run()