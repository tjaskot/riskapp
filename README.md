# riskapp
[![Build Status](https://travis-ci.org/tjaskot/riskapp.svg?branch=master)](https://travis-ci.org/tjaskot/riskapp)

The .travis.yml file contains a script portion of the automated build. This script portion defaults to bash without any kernel language env being set.

#User Defined Items
The user defined variables are located in riskapp.py. These variables are then instantiated into the html templates on an as needed basis.

#Html Reference
The index.html is the home page for the application and loads with window.onload browser function.

#Style Guide
The common css sits under the static/common.css file. All other style sheets have replicated naming convention for html and css. Example: about.html located under templates/about.html wwould have an associating about.css file located under static/about.css.

#Functionality Testing
There are two ways to test this application locally prior to pushing the changes to Travis CI. The Foreman server can be leveraged to host local server and test changes all on port 5000, or you can leverage Flask's internal hosting.
*Note: Travis CI will also test the build prior to deploying application to Heroku cloud in both the 2.7 and 3.5 versions of python.
