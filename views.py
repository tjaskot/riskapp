from flask import Flask, render_template, request, url_for, redirect, session

# User defined variables - views package
bkgrnd1 = "Department of Defense (DOD)"
bkgrnd2d0 = "- No solution mimicking"
bkgrnd2d1 = "- No software or simulation"
bkgrnd3 = "ODASA-CE analysis of projects"
poc1 = "Derek"
poc2 = "Leo"
poc4 = "Trevor"
poc3 = "Eric"

# Application Generated Routes
#@app.route('/')
def index():
    #Code to check the user session or browser cookie, otherwise redirect to login
    if 'username' in session:# and db.query.filter_by('id') != 'admin':
        return 'Logged in as {}'.format(session['username'])
    elif 'username' is 'admin':
        db.get_pass() #refer to something like this for password
        db.query.filter_by('password')
        return 'logged in'
    return redirect(url_for('login'))
    #return redirect(url_for('login'))#, variable=variable))

#@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userName = request.form['username']
        session['username'] = userName
        # db.session.add(userName)
        # db.session.commit()
        return redirect(url_for('home'))
    return render_template('login.html')
    # '''
    #     <form method='POST'>
    #         <p><input type=text name=username></p>
    #         <p><input type=submit value=Login></p>
    #     </form>
    # '''
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

#@app.route('/hello', methods=['GET'])
# This route is simply to test api/visually the uri endpoint with status 200 if success
def hello():
    return "Return 200"

#@app.route('/home')
def home():
    return render_template('index.html', bkgrnd1 = bkgrnd1, bkgrnd2d0 = bkgrnd2d0, bkgrnd2d1 = bkgrnd2d1, bkgrnd3 = bkgrnd3)

#@app.route('/generate', methods=['POST', 'GET'])
def generate():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = "Invalid username/password"
            return redirect(url_for('.not_found', error = error))
    return render_template('generate.html')

def signup():
    if request.method == 'POST':
        newUser = User(request.form['username'])
        db.session.add(newUser)
        db.session.commit()
        return(True)
    return render_template('signup.html')

#@app.route('/contacts')
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

    return render_template('contacts.html', poc1 = poc1, poc2 = poc2, poc3 = poc3, poc4 = poc4)

#@app.route('/about')
def about():
    return render_template('about.html')

#@app.route('/datafunction')
def datafunction():
    myVal = "myDataValue"
    return myVal

#@app.route('/logout')
def logout():
    # Remove user if ! in session
    session.pop('username', None)
    return redirect(url_for('index'))
