run these one by one in the project folder using cmd

python -m venv venv
venv\Scripst\activate
pip install -r requirments.txt
python manage.py makemigrations
python manage.py makemigrations base
python manage.py makemigrations users
python manage.py migrate
python manage.py runserver