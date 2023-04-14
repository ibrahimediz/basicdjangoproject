# basicdjangoproject
- source env/bin/activate  # ortamı aktif hale getirmek
- cd exercise/Demhat # egzersiz dosyalarına gidiş
- django-admin startproject website . #  django framework üzerinden bir proje başlatma
- python manage.py migrate # kurulumdan sonra veritabanını oluşturmak için 
- python manage.py createsuperuser
- python manage.py runserver 127.0.0.1:800..