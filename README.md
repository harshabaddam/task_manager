# Task Manager
Task manager is an application to create and assign tasks. \
**prerequisites**
* python3.6

Clone the repository \
`https://github.com/harshabaddam/task_manager.git`
Create virtual environment \
`virtualenv venv -p pyton3.6` \
activate the virtual environment \
`source venv/bin/activate` \
Install all dependencies in the virtual environment \
`pip install -r requirements.txt` \
Go the the **src** directory \
`cd src` \
Run the following commands to reflect models in database \
`python manage.py makemigrations` \
`python manage.py migrate` \
Create superuser to access the application \
`python manage.py createsuperuser` \
Run the project using following command
`python manage.py runserver 8000`
