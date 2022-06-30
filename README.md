# KMDB

# passo1 
 python -m venv venv 

 source venv/bin/activate

 pip install ipython 

 pip install djangorestframework

pip install django

 pip freeze > requirements.txt

django-admin startproject initial_files .

python manage.py startapp accounts
|_ coloca o app no settings.py

.gitignore
|_ venv, __pycache__ , db.sqlite3, .env
