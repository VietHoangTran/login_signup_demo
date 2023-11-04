python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn api.main:app --host 0.0.0.0 --port 8080

——————
django-admin startproject [name]

django-admin startapp [name]

python3 manage.py runserver

python3 manage.py makemigrations

 python3 manage.py migrate

 pip freeze   > requirements.txt