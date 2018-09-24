from flask import Flask, request
#request object allows us to access data in request user sent to server
#via python 

#POST refers to a methods parameter via request.form['param_name']

app = Flask(__name__)
app.config['DEBUG'] = True

"""GOAL 1:
Change Index Handler so it returns HTML that consists of
form that user can interact with"""

#Create global variable

form = """
<!DOCTYPE html>

<html>

<head>
    <title>Hello Flask Form</title>
</head>

<body>
    <form method="post">
        <label for salutation>Salutation:</label>
        <select id="salutation" name="salutation">
            <option value="Mr. ">Mr.</option>
            <option value="Miss ">Miss</option>
            <option value="Ms. ">Ms.</option>
            <option value="Ms. ">Ms.</option>
        </select>
        <p><label for first_name>First Name:</label>
        <input id="first_name" type="text" name="user_name"></p>
        <p><label for origin_city>City of Origin:</label>
        <input id="origin_city" type="text" name="origin_city"></p>
        <input type="submit">

    </form>

</body>
</html>

"""

@app.route("/")

def index():
    return form


"""GOAL 2:
Write code to handle our submission to allow a form
to be processed (can customize values to be printed)"""

@app.route("/form-inputs")
def display_form_inputs():
    return form

@app.route("/form-inputs", methods=['POST'])
def print_form_values():
    #use get request object by using request.args.get with name
    resp = ""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])

    return resp


"""
#For POST request, data not exposed in URL:
http://127.0.0.1:5000/hello
"""


app. run()