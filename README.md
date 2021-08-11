# intial-Data-Base
## Steps: 
# Configuration
1. `$ mkdir drf-api`
2. `$ cd drf-api`
3. `$ poetry init -n`
4. `$ poetry add djangorestframework`
5. `$ poetry add --dev black`
6. `$ poetry shell`

# create a new project
8. `(.venv) $ django-admin startproject carsEcommerce .`
9. `(.venv) $ python manage.py migarate`
10. `(.venv) $ python mange.py runserver`

> Don’t forget to include the period (.) at the end which installs the code in our current directory. If you do not include the period, Django will create an additional directory by default.
 
# First app
create a player app
1.  `(.venv) $ python manage.py startapp cars`
2.  go project settings add the new app to our INSTALLED_APPS configuration.
# Models
1.  open player/models.py add class and what we need
Since we created a new database model we need to create a migration file to go along with it, then update our database.
1.  `python manage.py migrate`
2.  `(.venv) $ python manage.py makemigrations cars`
3.  `(.venv) $ python manage.py createsuperuser`
4.  username: mohammad password: 0000
5.  open admin apps import the model and register
6 . run the server and add player 

# now REST part 

# Django REST Framework
18. project setting , Add it to the INSTALLED_APPS config in our settings.py file
19. project setting , add Permissions to use Rest Framework
# URL
add settings , installapp => 'rest_framework'. allow use to run it as rest app , add restframewoek dir  
20. open the url project ; add url for app and app url file in the app and add some url and class in view app
21. add file in app serializers.py and add class to it , link between view and data from database
> serializers ; somthing between database and view , convert it in JSON style
22. open view from app => from rest get stuff

for images we need packegs: pillow