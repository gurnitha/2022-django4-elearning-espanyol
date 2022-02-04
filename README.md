# 2022-django4-elearning-espanyol
This is my exercise base on My Learning on Udemy

Github repository: https://github.com/gurnitha/2022-django4-elearning-espanyol


### 1. INITIAL SETUP
--------------------

#### 1.1 Create and clone Github repository

```py

# Clone Github repository

E:\workspace\django-2022\ESPANYOL\2022-django4-elearning-espanyol
λ git clone git@github.com:gurnitha/2022-django4-elearning-espanyol.git
Cloning into '2022-django4-elearning-espanyol'...
Enter passphrase for key '/c/Users/hp/.ssh/id_rsa':
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (5/5), done.

```


#### 1.2 Create venv and installing django version 4.0


```py
# 1. Create virtual environment
λ python -m venv venv3940 --promp elearning-esp

# 2. Activate venv
λ venv3940\Scripts\activate.bat

# 3. Install django
(elearning-esp) λ pip install django==4.0

# 4. Upgrade pip
(elearning-esp) λ python.exe -m pip install --upgrade pip

# Files: new/changed

        modified:   README.md
```


### 2. CREATE DJANGO PROJECT
----------------------------

#### 2.1 Create django project

```py

# 1.Create django project
(elearning-esp) λ django-admin startproject Usuarios .

# 2. Run the server
(elearning-esp) λ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 04, 2022 - 08:38:46
Django version 4.0, using settings 'Usuarios.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

# 3. Open the project in browser
http://127.0.0.1:8000/

# Files: new/changed

        modified:   README.md
        new file:   Usuarios/__init__.py
        new file:   Usuarios/asgi.py
        new file:   Usuarios/settings.py
        new file:   Usuarios/urls.py
        new file:   Usuarios/wsgi.py
        new file:   manage.py
```


### 3. TURNING DJANGO TO REAL MVC - CREATING LOGIN SYSTEM
----------------------------------------------------------


#### 3.1 Create IndexController

```py
# 1. Create folder
λ mkdir Usuarios\Controllers

# 2. Create file
λ touch Usuarios\Controllers\IndexController.py

# Files: new/changed
        modified:   README.md
        new file:   Usuarios/Controllers/IndexController.py
        modified:   Usuarios/urls.py

# NOTE: :)
```

#### 3.2 Create Template Views

```py

# 1. Create folder
λ mkdir templates\views\index

# 2. Create file and add text
λ touch templates\views\index\index.html

# 3. Activating django template in settings.py
'DIRS': [os.path.join(BASE_DIR, 'templates')],

# 4. Modify IndexController, urls.py
See the repository

# Files: new/changed
        modified:   README.md
        modified:   Usuarios/Controllers/IndexController.py
        modified:   Usuarios/settings.py
        modified:   Usuarios/urls.py
        new file:   templates/views/index/index.html

# NOTE: :)
```

#### 3.3 Adding html template to index

```py
# Files: new/changed
        modified:   README.md
        modified:   templates/views/index/index.html

# NOTE: :)
```

#### 3.4 Add and load static files

```py
# Files: new/changed
        modified:   README.md
        modified:   Usuarios/settings.py
        new file:   static/css/bootstrap-grid.css
        ...
        new file:   static/js/bootstrap.min.js
        modified:   templates/views/index/index.html

# NOTE: :)
```

#### 3.5 Modified index using include

```py
# Files: new/changed
        renamed:    static/css/style.css -> static/css/custom.css
        new file:   templates/views/default/footer.html
        new file:   templates/views/default/header.html
        modified:   templates/views/index/index.html

# NOTE: :)
```

#### 3.6 Adding sliders and about page

```py
# Files: new/changed

        modified:   Usuarios/Controllers/IndexController.py
        modified:   Usuarios/urls.py
        new file:   static/css/style.css
        new file:   static/js/jquery-3.3.1.min.js
        modified:   templates/views/default/footer.html
        modified:   templates/views/default/header.html
        new file:   templates/views/index/about.html
        modified:   templates/views/index/index.html

# NOTE: :)
```

#### 3.7 Setting up database

```py

# 1. Install mysql driver
(elearning-esp) λ pip install mysqlclient

# 2. Install django environ
(elearning-esp) λ pip install django-environ

# 3. Create and setup .env
Can not view it here 

# 4. Create and connect db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# Files: new/changed

        modified:   .gitignore
        modified:   Usuarios/settings.py
        new file:   static/images/Python-portada.png
        new file:   templates/404.html
        modified:   templates/views/default/header.html
        modified:   templates/views/index/index.html

# NOTE: :)
```

#### 3.8 Create superuser and link to login to admin panel

```py

# 1. Create migrations
(elearning-esp) λ python manage.py makemigrations
No changes detected

# 2. Apply migrations
(elearning-esp) λ python manage.py migrate

# 3. Create superuser
(elearning-esp) λ python manage.py createsuperuser

# Files: new/changed

        modified:   templates/views/default/header.html

# NOTE: :)
```

#### 3.9 Create a new app 'App'

```py

# 1. Create a new app
(elearning-esp) λ python manage.py startapp App

# 2. Move Controller to App
(elearning-esp) λ python manage.py migrate

# 3. Modified the urls
from App.Controllers.IndexController import IndexController

# 4. Testing runserver

:)

# Files: new/changed

        renamed:    Usuarios/Controllers/IndexController.py -> App/Controllers/IndexController.py
        new file:   App/__init__.py
        new file:   App/admin.py
        new file:   App/apps.py
        new file:   App/migrations/__init__.py
        new file:   App/models.py
        new file:   App/tests.py
        new file:   App/views.py
        modified:   README.md
        modified:   Usuarios/urls.py
# NOTE: :)
```

#### 3.10 Create login template

```py

# Files: new/changed
        modified:   README.md
        modified:   Usuarios/urls.py
        new file:   static/css/login.css
        new file:   templates/admin/login.html
        modified:   templates/views/default/header.html

# NOTE: :)
```

#### 3.11 Modified login template

```py

# Files: new/changed
        modified:   static/css/login.css
        modified:   templates/admin/login.html

# NOTE: :)
```


### 4. DJANGO MODEL
-------------------


#### 4.1 Create models: Categorias, Cursos

```py

# Files: new/changed

        modified:   App/admin.py
        new file:   App/migrations/0001_initial.py
        modified:   App/models.py
        modified:   README.md
        modified:   Usuarios/settings.py
        new file:   images/curso/mobile-5.PNG

# NOTE: :)
```


#### 4.2 Register models to admin and define model's display in admin panel

```py


# Files: new/changed

        modified:   App/admin.py
        modified:   README.md
        modified:   Usuarios/settings.py
        modified:   Usuarios/urls.py
        new file:   media/images/curso/mobile-5.PNG
        new file:   media/images/curso/samsung-tv.PNG

# NOTE: :)
```


