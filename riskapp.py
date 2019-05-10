### Imported packages ###
# Flask
# render_template
# request
# redirect
# url_for
# os
# sys 
# plotly
#########################

from flask import Flask, render_template, request, url_for, redirect
import os, sys, plotly, json
import plotly.plotly as py
import plotly.graph_objs as go
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#   import MySQLdb #If future work for MySQL is wanted with database

app = Flask(__name__)

# Define User Specific Variables
bkgrnd1 = "Department of Defense (DOD) software development issues drive cost overruns and delay in capability delivery Majority of DOD Major Defense Acquisition Programs (MDAPs) rely on software development to varying degrees ODASA-CE does not have reliable systems / tools available to conduct entity driven tradeoff analysis or risk assessment of software development projects"
bkgrnd2d0 = "- No solution mimicking the DOD Architecture Framework (DODAF) is readily available"
bkgrnd2d1 = "- No software or simulation based solution is readily available Objective: Develop, document, and deliver baseline model of Department of the Army (DA) software development teams in order to support"
bkgrnd3 = "ODASA-CE analysis of projects including validation and verification (V/V) of program manager projections, staffing policy development, and interdependent processes exploration"
poc1 = "Derek Eichin - Customer and Project Owner - Operations Research Analyst (ODASA)"
poc2 = "Leo Pacatan - Product Owner, Contributor - Systems 699 Student - Biography:  Received a Bachelor of Science in Statistics with a minor in Business Administration from University of North Florida in May 2008.  Has worked as a Management Analyst for the Department of the Army for the past ten years, providing manpower and force management analysis on various major commands and their programs.  His Analyst work is comprised of building trend analysis, conducting studies, and developing models in determining required manpower strength.  Will complete a Master’s of Science in Operations Research with a concentration in Data Analytics from George Mason University in May 2019, along with a graduate certificate in Data Analytics."
poc4 = "Trevor Jaskot - Developer, Contributor - Systems 699 Student - Biography:  Received a Bachelor of Science in Physics from George Mason University in May 2015.  I have worked with the government for 7 years, 5 as a contractor and 2 as a federal civilian. I am currently working for JPMorgan Chase as a Cloud Software Engineer in the Global Technology Organization. I specialize in large scale cloud platform development and have created 2 patents for JPMorgan. I consult with many third party vendors and work to continually expand on providing Customer Service to Developers and Clients across the firm. Most recently I have worked on an Identity and Authorization automation project whereby all platform Identity and Access is automatically integrated with Cyber Regulatory demands while in tandem being completely tokenized and abstracted to the end-user. Will complete a Master’s of Science in Systems Engineering (C4I) Concentration in Electrical Engineering from George Mason University in May 2019."
poc3 = "Eric Jones - Stochastic Model Owner, Contributor - Systems 699 Student - Biography:  Received a Bachelor of Science in Civil Engineering with a certificate in advanced leadership studies from Texas A&M University in May 2015.  Most recently worked as an Operational Research Analyst at Systems Planning and Analysis, Inc. (SPA) for the past three years supporting decision-makers across a variety of government organizations including: Royal Australian Navy, Australian Defence Force, U.S. Navy N81 and N97, Office of Naval Research, DARPA, Department of Defense CIO, U.S. Coast Guard, and U.S. Pacific Command. This work spans the breadth of operations research tool sets in exploring trade-off analyses, informing requirements, and conducting performance assessments. Additionally, Eric is an Engineer in the U.S. Army Reserves. He will complete a Master’s of Science in Operations Research from George Mason University in May 2019."

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
    #return redirect(url_for('login'))
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
            return redirect(url_for('notfound.html', error=error))
    return render_template('generate.html')

@app.route('/contacts')
#Syntax of python flask does not require variable from redirect to be passed into the below def function
def contacts():
    return render_template('contacts.html', poc1=poc1, poc2=poc2, poc3=poc3, poc4=poc4)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/datafunction')
def datafunction():
    myVal = ""
    return myVal

#This commented /generatesomethingelse app.route is for another call made from the javascript if an ajax call is wanted to post data anywhere for any purpose.
#@app.routeasl;dkfj('/generatesomethingelse', methods=['POST'])
#def genStuff():
#    layout = {
#        'xaxis': {
#            'showticklabels': False,
#            'showgrid': False,
#            'zeroline': False,
#        },
#        'yaxis': {
#            'showticklabels': False,
#            'showgrid': False,
#            'zeroline': False,
#        },
#        'shapes': [
#            {
#                'type': 'path',
#                'path': 'M 0.235 0.5 L 0.24 0.65 L 0.245 0.5 Z',
#                'fillcolor': 'rgba(44, 160, 101, 0.5)',
#                'line': {
#                    'width': 0.5
#                },
#                'xref': 'paper',
#                'yref': 'paper'
#            }
#        ],
#        'annotations': [
#            {
#                'xref': 'paper',
#                'yref': 'paper',
#                'x': 0.23,
#                'y': 0.45,
#                'text': '50',
#                'showarrow': False
#            }
#        ]
#    }
#    # we don't want the boundary now
#    base_chart['marker']['line']['width'] = 0
#    
#    fig = {"data": [base_chart, meter_chart],
#           "layout": layout}
#    py.iplot(fig, filename='gauge-meter-chart')
#
#    return render_template('pythonChart.html')

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
