myvenv\Scripts\activate
python -m http.server 8001 --cgi
http://127.0.0.1:8001/blog/templates/blog/login.html
http://127.0.0.1:8001/login.html
http://127.0.0.1:8000/
python manage.py runserver

python manage.py makemigrations sample_app
python manage.py migrate sample_app