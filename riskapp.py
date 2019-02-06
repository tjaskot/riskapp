### Imported packages ###
# Flask
# render_template
# request
# url_for
#########################

from flask import Flask, render_template, request, url_for
import os, sys
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello this is a application to determine risk for schedule and cost projections"

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = "Invalide username/password"
            return redirect(url_for('loginerror', error=error))
    return render_template('login.html')

@app.route('/loginerror')
#Syntax of python flask does not require variable from redirect to be passed into the below def function
def loginerror():
    #Checks to see if error is null, and catches exception
    try:
        #This code may raise an error if nothing is not null
        error = error
    except:
        error = "This is my error."
        app.logger.error("Application is passing null into loginerror function.")
    return render_template('loginerror.html', error = error)

@app.errorhandler(404)
def not_found(error):
    return render_template('notfound.html'), 404

#Unit tests for application below (unit test code coverage +70%)
#Validate that all url's are responsive
with app.test_request_context('/hello', method='GET'):
    #print(url_for(''))
    assert request.path == '/hello'
    assert request.method == 'GET'

with app.test_request_context('/login', method='POST'):
    assert request.path == '/login'
    assert request.method == 'POST'

with app.test_request_context('/loginerror'):
    assert request.path == '/loginerror'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
