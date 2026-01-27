### Django Blog venv 
[Django Blog Venv](https://github.com/pollyolly/djangoblog-venv)

### Django Blog Deployment on VPS
[Django Blog VPS](https://medium.com/aws-tip/setup-and-start-a-django-project-in-m1-7c36f96c3088)

### Django Blog Deployment on [Python Anywhere](pythonanywhere.com)
Virtualenv
```
$mkvirtualenv --python=python3.13 djangoblog #Ceate Virtual Environment with specified python version
$pip freeze > requirements.txt #Create List of Installed Modules
$pip install -r requirements.txt #Install Modules from Requirements List
$workon <my_virtual_environment> #Activate Created Virtual Environment
$lsvirtualenv #List Created Virtual Environment
$rmvirtualenv <my_virtual_environment>
```
Setup on Pythonanywhere
```
```
### Fix Install Requirements
Install Requirements
```
zope.interface #Remove this from requirements.txt Not Required in python < 13
```
```
$pip install bleach #Remove this from requirements.txt and install without version
$pip install pillow #Remove this from requirements.txt and install without version
$pip install PyYAML #Remove this from requirements.txt and install without version
$pip install -r requirements.txt
```
Install Django modules
```
$pip install django
$pip install channels
$pip install django-jazzmin
$pip install django-import-export
$pip install django-tinymce
$pip install django-debug-toolbar
$pip install pillow
$pip install whitenoise
$pip install django-auto-logout
```
### Heroku Requirements
```
Procfile
requirements.txt ($pipenv run pip freeze > requirements.txt)
runtime.txt

```
### FrontEnd
```
- getbootstrap: https://getbootstrap.com/docs/5.1/examples/album/
```
### Deployment
[Django Deployment](https://github.com/pollyolly/DJANGO-NOTE)

### Tutorials
[django-auto-logout](https://pypi.org/project/django-auto-logout/)

[best-free-wysiwyg-editor-python-django-admin-panel-integration](https://blog.devgenius.io/best-free-wysiwyg-editor-python-django-admin-panel-integration-d9cb30da1dba)

[customize-django-admin-python](https://realpython.com/customize-django-admin-python/)

[django-admin-cookbook](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/export.html)

