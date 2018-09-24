from flask import Flask, request
#request object allows us to access data in request user sent to server
#via python 

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
    <form action="/hello" method="post">
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

time_form = """
    <style>
        .error {{
            color: red;
            font-weight: 800;
        }}
    </style>

    <h1>Validate Time</h1>
    <form method='POST'>
        <label for="hours">Hours (24-hour format)</label>
            <input name="hours" type="text" id="hours" value='{hours}'>
        <p class="error">{hours_error}</p>
        <label for="minutes">Minutes</label>
            <input name="minutes" type="text" id="minutes" value='{minutes}'>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Validate">
    </form>
"""

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


@app.route("/")
def index():
    return form

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='', minutes='', minutes_error='')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = "Hour value is out of range (0-23)"
            hours = ''
    
    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = "Minutes value out of range (0-59)"
            minutes = ''

    if not minutes_error and not hours_error:
        return "Success!"
    else:
        return time_form.format(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)


app.run()
