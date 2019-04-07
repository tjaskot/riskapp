### Riskapp ###
# Markdown is used for github label tagging

# Travis-ci build tag
[![Build Status](https://travis-ci.org/tjaskot/riskapp.svg?branch=master)](https://travis-ci.org/tjaskot/riskapp)

The build tag is to show visual status of the current build in Master branch of the github repository. The .travis.yml file contains a script portion of the automated build. This script portion defaults to bash without any kernel language env being set.

#User Defined Items
The user defined variables are located in riskapp.py. These variables are then instantiated into the html templates on an as needed basis.
Because virtual environments are being used to test the functionality both in python 2.7 and python 3.5, then there will be a 'riskapp' folder under the main folder that contains basic linux directories like lib/ and bin/.

#Html Reference
The index.html is the home page for the application and loads with window.onload browser function.

#Style Guide
The common css sits under the static/common.css file. All other style sheets have replicated naming convention for html and css. Example: about.html located under templates/about.html wwould have an associating about.css file located under static/about.css.

#Functionality Testing
There are two ways to test this application locally prior to pushing the changes to Travis CI. The Foreman server can be leveraged to host local server and test changes all on port 5000, or you can leverage Flask's internal hosting.
*Note: Travis CI will also test the build prior to deploying application to Heroku cloud in both the 2.7 and 3.5 versions of python.

#Notes
When using flask to test locally, there will be an <app_name>.pyc file created for the compiled code which flask hosts on the local server. This is expected and normal. If you do not want to push this file to your git repo, then add *.pyc to your .gitignore file.

When using foreman to test locally, there will be a folder with <app_name> created. This is expected and leveraged by foreman to create a local host version of your application prior to pushing. If you want to not push this folder then you must modify the .gitignore file to exclude the <app_name> folder.

Viewing all current packages installed locally, a developer can use "pip freeze > requirements.txt" that creates a file with all the necessary packages later leveraged by python flask during hosted testing.

You can also leverage the commented code to post values to a database. This application is not connected to a database because of time constraints, feel free to add community additions.

The reason javascript plotly charts were used is for ease of interaction with css formatting. Both python gauge charts and javascripts charts are functional. The python charts are commented out, but if you would like to fork this repo and use python instead of javascript to create the charts, then uncomment the ajax POST in the corresponding javascript file and leveverage the commented function "def genStuff()" in riskapp.py. 
