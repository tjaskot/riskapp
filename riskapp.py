### Imported packages ###
# Flask
# render_template
# request
# redirect
# Blueprint
# url_for
# session
# os
# sys
# plotly
# email (mime)
# jsonify
# send_file
# collections
# logging
# importlib
# markupsafe
#########################

from flask import Flask, render_template, request, url_for, redirect, jsonify, send_file, session #TODO: , Blueprint
import os, sys, plotly, json
import chart_studio.plotly as py
import plotly.graph_objects as go
import importlib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from markupsafe import escape

#TODO: move to folder riskapp, rn using just app
# riskapp = Blueprint('riskapp', __name__)
app = Flask(__name__)

#TODO: temp secret key
app.secret_key = 'secret'

# Define User Specific Variables
appName = "RiskApp Tool"
bkgrnd1 = "Department of Defense (DOD)"
bkgrnd2d0 = "- No solution mimicking"
bkgrnd2d1 = "- No software or simulation"
bkgrnd3 = "ODASA-CE analysis of projects"
poc1 = "Derek"
poc2 = "Leo"
poc4 = "Trevor"
poc3 = "Eric"

# create logger
#TODO: doubles out because of example.log
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# set logging file output configuration
#logger.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
# create console handler and set level to debug
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to consoleHandler
consoleHandler.setFormatter(formatter)
# add ch to logger
logger.addHandler(consoleHandler)
# log bsaic info
logger.info("Initial Startup of: " + appName)
logger.debug('This message should go to the log file')
logger.warning('Warning: Test')

@app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

# Application Generated Routes
@app.route('/')
def root():
    #Code to check the user session or browser cookie, otherwise redirect to login
    if 'username' in session:
        return 'Logged in as {}'.format(escape(session['username']))
    return redirect(url_for('login'))
    #return redirect(url_for('login'))#, variable=variable))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return '''
        <form method='POST'>
            <p><input type=text name=username></p>
            <p><input type=submit value=Login></p>
        </form>
    '''
    #    return render_template('login.html')

        # Old code without session
        #login = request.form['username']
        #password = request.form['password']
        #if login == "admin" and password == "admin":
        #    return redirect(url_for('home'))
        #else:
        #    error = "Incorrect Information. Please Try Again."
        #    return render_template('login.html', error=error)
    #else:
    #    return render_template('login.html')

@app.route('/hello', methods=['GET'])
# This route is simply to test api/visually the uri endpoint with status 200 if success
def hello():
    return "Return 200"

@app.route('/home')
def home():
    return render_template('index.html', bkgrnd1=bkgrnd1, bkgrnd2d0=bkgrnd2d0, bkgrnd2d1=bkgrnd2d1, bkgrnd3=bkgrnd3)

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = "Invalid username/password"
            return redirect(url_for('.not_found', error=error))
    return render_template('generate.html')

@app.route('/contacts')
#Syntax of python flask does not require variable from redirect to be passed into the below def function
def contacts():
    sendEmail = 'false'
    if sendEmail == 'true':
        requestor = request.form['siteOwner']
        #Change the string into list for list concatanation later in function
        recipient = [requestor]
        cc = ['trevor186@msn.com']
        bcc = []
        sender = 'myFlowerShop@outlook.com'
        msg = MIMMultipart('alternative')
        msg['Subject'] = 'Flower Info Request'
        msg['From'] = sender
        msg['To'] = ",".join(recipient)
        msg['CC'] = ",".join(cc)
        msg['BCC'] = ",".join(bcc)
        recipient += cc + bcc
        #More detail in e-mail content
        email_body = None
        email_body_header = ' '
        email_body_header += '<html><head></head><body>'
        email_body_header += '<style type="text/css"></style>'
        email_body_header += '<br><h2>Hey</h2><p>Email Header</p><br><p>Requested Info:</p><br>'
        email_body_content = ' '
        email_body_content += '<p> + requestor + </p>'
        email_body_footer = ' '
        email_body_footer += '<br>Thank you.'
        email_body_footer += '<br><p>R/</p><p>Flower Support</p><br>'
        html = str(email_body_header) + str(email_body_content) + str(email_body_footer)
        part = MIMEText(html, 'html')
        msg.attach(part)
        s = smtplib.SMTP('mailhost.flowershop.com')
        s.sendmail(sender, recipient, msg.as_string())
        s.quit()

    return render_template('contacts.html', poc1=poc1, poc2=poc2, poc3=poc3, poc4=poc4)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/datafunction')
def datafunction():
    myVal = "myDataValue"
    return myVal

@app.errorhandler(404)
def not_found(error):
    ##Checks to see if error is null, and catches exception
    #try:
    #    #This code may raise an error if nothing is not null
    #    error = error
    #except:
    #    error = "This is my error."
    #    app.logger.error("Application is passing null into loginerror function.")
    return render_template('notfound.html'), 404

@app.route('/logout')
def logout():
    # Remove user if ! in session
    session.pop('username', None)
    return redirect(url_for('index'))

### Unit tests ###
# For application below (unit test code coverage +70%)
# Validate that all url's are responsive and identify as themselves
with app.test_request_context('/hello', method='GET'):
    #print(url_for(''))
    assert request.path == '/hello'
    assert request.method == 'GET'

with app.test_request_context('/generate', method='POST'):
    assert request.path == '/generate'
    assert request.method == 'POST'

with app.test_request_context('/contacts'):
    assert request.path == '/contacts'

with app.test_request_context('/about'):
    assert request.path == '/about'

with app.test_request_context('/login', method='POST'):
    assert request.path == '/login'
    assert request.method == 'POST'

with app.test_request_context('/home'):
    assert request.path == '/home'

with app.test_request_context('/datafunction'):
    assert request.path == '/datafunction'
###################

#TODO: this should do in main.py, and riskapp.py should be a blueprint template folder app
#   This file is being used as both main.py and riskapp.py and some overlap in init.py
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    #app.run works because __init__ created app object
    app.run(host='0.0.0.0', port=port)
