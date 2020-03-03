
Todo-Django A django web app for basic task lists that are segmented by user.


INSTALLATION

Linux: virtualenv should be installed

virtualenv -p python3 .venv

source .venv/bin/activate

pip install -r requirements.txt



For the first time don't forget:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
