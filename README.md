# GITHUB - RENDER - POSTGRES - DJANGO

## This document explains the processes to:

### Create a postgres database in Render

* Link to the postgres database in Django
* Create a new Github repository for the Django project
* Maintain the Django project in Github
* Create a web service for Django in Render
* Open a browser to the Django web app
* Serve static files using Whitenoise

### The URL to the Django-Render web site

[Render URL](https://django-postgres-render-ldgq.onrender.com)

### How to serve Django static files on Render

[Django Static files on Render](https://docs.render.com/deploy-django)

### Create a postgres database in Render

- Login to Render.com
- Select New+ → PostgresSQL

```
Unique Name: drbaz-database

Region: Frankfurt

Instance Type: For hobby projects
```

- Select Create Database
- Click on the database name and review the Connections data

### Link  database to Django

- Create a simple Django project in VSCode
- Create a virtual environment (.venv)
- Using pip install

```
dj-database-url
django-environ
guincorn
psycopg2-binary
pip freeze > requirements.txt
```

- Add a url to urls.py (project)
- Create a views.py and add a view to views.py (project)
- Create a templates folder in the same folder as manage.py and a few html files as referenced in the views.py file
- edit the settings.py file, TEMPLATES section to read

```
"DIRS": ['templates'],
```

- Create a static/css folder in the same folder as manage.py and add style.css

```css
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    display: grid;
    place-content: center;
    font-size: 2rem;
    background-color:lightgrey;
    color:blueviolet;

}
h1,p {
    text-align: center;
}

a {
    color:red;
}
```

- Add the following to settings.py

```
import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default':dj_database_url.parse(env('DATABASE_URL'))
}

```

- Add the Django app name to settings.py in the INSTALLED_APPS dictionary
- Create a .env file and add the following

```
DATABASE_URL= this is the external database url from Render with NO surrounding quotes 

SECRET_KEY = the secret key from Django settings.py

DEBUG=True
```

- Test the Django project by migrating and creating superuser

### Create a Github Repository for the Django Project

- Using VSCode, select the GitHub icon
- Initialise repository
- Enter commit message
- Select Commit
- Select Publish
- Check new repository on Github is main branch
- Any changes to code shpould be committed and sync'd tomaij or a new branch.

### Create a Render Web Service for Django Project

- Go to Render Dashboard and select New+ → Web Service
- Select Build and Deploy from Git Repository and select Next
- Under GitHub, select Configure Account - GitHub Render page displays
- Under Repository Access, select repository to be accesses by Render
- Select Save
- The Render Create a New Web Service page will be displayed and the GitHub repository is listed
- Select Connect alongside the repository name
- The deploying web service page is displayed
- Enter a name for teh web service
- Set Region to Frankfurt
- Set Branch to Main - but select most recent branch if updated code
- Set Start Command  to

```
gunicorn myproject.wsgi:application
```

as stated in settings.py, but replace last . with :

- Set Instance Type to Hobby Project
- Set Instance Variables
-

```
PYTHON_VERSION = 3.12.2
DATABASE_URL = internal url from Render Database Dashboard
SECRET_KEY = secret key from .env
DEBUG=False
```

- Select Create Web Service button
- Log window displays and shows deployment progress. Takes a few minutes.
- Deployment completed when “Your Service is Live” message shows
- **REMEMBER to change deployment GitHub branch if not using main**

### Render URL on Browser

- Go to Render Dashboard
- Select the appropriate service name
- Copy the blue url and paste into browser
- Your Django project is displayed, but static files will not served yet

### Making changes to code in VSCode

- Change code and test in VScode.
  - Local web service will still work but will connect to Render Postgres Database.
- Commit to GitHub branch main and sync ( or new branch )
- Set  Render deployment to main GitHub branch or set it to most recent branch
- Render should auto-deploy unless there’s an error.
- Fix error and manually Redeploy in Render

### Set up static file serving with Whitenoise

```
pip install whitenoise

pip freeze > requirements.txt
```

- Open settings.py in your project’s main directory
- Add the following to the MIDDLEWARE list, immediately after SecurityMiddleware:

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]
```

Make the following modifications to settings.py:

```
STATIC_URL = 'static/'
if DEBUG:   
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

```

- Commit and sync to GitHub
- Django web site will be rendered as per your .css file
