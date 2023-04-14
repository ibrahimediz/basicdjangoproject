# basicdjangoproject
- source env/bin/activate  # ortamı aktif hale getirmek
- cd exercise/Demhat # egzersiz dosyalarına gidiş
- django-admin startproject website . #  django framework üzerinden bir proje başlatma
- python manage.py migrate # kurulumdan sonra veritabanını oluşturmak için 
- python manage.py createsuperuser # süper kullanıcı oluşturmak için
- python manage.py runserver 127.0.0.1:800.. # web sitesini yayınını başlatmak için
- python manage.py startapp [uygulama ismi] # web sitesine eklemek için uygulama oluşturmak
- python manage.py makemigrations musteri # ilgili uygulamanın vertibanı değişikliklerini toplar
- python manage.py migrate # toplanan değişiklikler veri tabanına yansıtılır