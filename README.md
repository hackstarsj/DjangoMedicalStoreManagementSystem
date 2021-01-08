# DjangoMedicalStoreManagementSystem



## Live API URL
<a href="https://medicalstoreapi.herokuapp.com/api/">https://medicalstoreapi.herokuapp.com/api/</a>

## Live Project LINK 
<a href="https://pacific-falls-18076.herokuapp.com/">https://pacific-falls-18076.herokuapp.com/</a>

## Login DETAILS
<pre>USername : admin</pre>
<pre>Password : admin</pre>

# For Deploy React APP in HEROKU

## Signup in HEROKU
<pre>https://dashboard.heroku.com/apps</pre>

## Download Heroku Login
<pre>https://devcenter.heroku.com/articles/heroku-cli#download-and-install</pre>

## Login To Heroku
<pre>heroku login</pre>

## Create Project in Heroku
<pre>heroku create PROJECT_NAME</pre>

## Create runtime.txt
</pre>ADD Python Version in this File (E.G python-3.7.4)</pre>

## Create requirements.txt and Add Libraries
<pre>CHECK requirements.txt File</pre>

## Create Procfile
<pre>web: gunicorn PROJECT_LOCATIOn.wsgi --log-file - (E.G : web: gunicorn DjangoMedicalStoreManagementSystem.wsgi --log-file -)</pre>
 
 ## Change Settings.py Setting
 <pre>First Allowed HOST DOMAIN NAME </pre>
 <pre>Second ADD Middleware "whitenoise.middleware.WhiteNoiseMiddleware" </pre>
 <pre>Third ADD CORS_ORIGIN_WHITELIST = ["ADD DOMAIN HERE WITH HTTP URL (E.G : http://localhost:3000)"] </pre>
 ## FOURTH ADD THIS SETTING in settings.py 
<pre>
import dj_database_url
prod_db=dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
</pre>
##================PROJECT DETAIL============

DjangoMedicalStoreManagementSystem Server Side

For Project Tutorial Please Follow Video : https://www.youtube.com/playlist?list=PLb-NlfexLTk_lsm7qMjMamK51bTAbQ3mH

### For Client Side React Project Follow This Link.

<a href="https://github.com/hackstarsj/DjangoMedicalStoreFrontEndInReactJS">Django Medical Store management System Client Side in React JS</a>


<br>
<h4>ER Diagram</h4>

<img src="https://github.com/hackstarsj/DjangoMedicalStoreManagementSystem/blob/master/screenshots/ER_DIAGRAM.png"/>

## How Django and React Works.
<img src="https://github.com/hackstarsj/DjangoMedicalStoreManagementSystem/blob/master/django-react.png"><br>