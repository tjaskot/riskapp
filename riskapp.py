### Imported packages ###
# Flask
# render_template
# request
# redirect
# url_for
# os
# sys
# plotly
# email (mime)
# jsonify
# send_file
# collections
# logging
# importlib
#########################

from flask import Flask, render_template, request, url_for, redirect, jsonify, send_file
import os, sys, plotly, json
import chart_studio.plotly as py
import plotly.graph_objects as go
import importlib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#   import MySQLdb #If future work for MySQL is wanted with database

app = Flask(__name__)

# Define User Specific Variables
appName = "RiskApp Tool"
bkgrnd1 = "Department of Defense (DOD) software development issues drive cost overruns and delay in capability delivery Majority of DOD Major Defense Acquisition Programs (MDAPs) rely on software development to varying degrees ODASA-CE does not have reliable systems / tools available to conduct entity driven tradeoff analysis or risk assessment of software development projects"
bkgrnd2d0 = "- No solution mimicking the DOD Architecture Framework (DODAF) is readily available"
bkgrnd2d1 = "- No software or simulation based solution is readily available Objective: Develop, document, and deliver baseline model of Department of the Army (DA) software development teams in order to support"
bkgrnd3 = "ODASA-CE analysis of projects including validation and verification (V/V) of program manager projections, staffing policy development, and interdependent processes exploration"
poc1 = "Derek"
poc2 = "Leo"
poc4 = "Trevor"
poc3 = "Eric"

app.logger.addHandler(logging.StreamHandler())
app.logger.info("Initial Startup of: " + appName)

@app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

# Application Generated Routes
@app.route('/')
def root():
    #Code to check the user session or browser cookie, otherwise redirect to login
    #Session = sessionmaker(bind=engine)
    #session = Session()
    #user = User("admin","password")
    #session.add(user)
    #if (username = request.cookies.get('username')):
    #    return url_redirect('/index')
    #else:
    #    return render_template('login.html', error=error)
    #return redirect(url_for('.login', variable=variable))
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        if login == "admin" and password == "admin":
            return redirect(url_for('home'))
        else:
            error = "Incorrect Information. Please Try Again."
            return render_template('login.html', error=error)

@app.route('/hello', methods=['GET'])
# This route is simply to test api/visually the uri endpoint with status 200 if success
def hello():
    return "Hello this will provide a demonstration of the application. It will show you the projections for a sample set of data and provide you with instructions on how to generate your own relative data sets."

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
    sendEmail = false
    if [sendEmail == true]:
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
    myVal = ""
    return myVal

#@app.route('/putValuesIntoDatabase', methods=['POST'])
#def putDBValues():
#    print('i want to set values in a database')
#    #Open database connection
#    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
#    #prepare a cursor object using cursor() method
#    cursor = db.cursor()
#
#    #Prepare SQL query to INSERT a record into the database.
#    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#             LAST_NAME, AGE, INCOME)
#             VALUES ('name', 'person', 20, 2000)"""
#    try:
#       # Execute the SQL command
#       cursor.execute(sql)
#       # Commit your changes in the database
#       db.commit()
#    except:
#       # Rollback in case there is any error
#       db.rollback()
#    #disconnect from server
#    db.close()

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

#Unit tests for application below (unit test code coverage +70%)
#Validate that all url's are responsive and identify as themselves
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

# If environment is needed by host, then define variables below
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
