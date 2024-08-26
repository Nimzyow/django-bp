Must use serializer to validate datetime of slept_at

To create a django project with config as name of where all settings are

```bash
django-admin startproject config .
```

seed database

```bash
python manage.py seed_user
python manage.py seed_sleep
```

URL's

* /signup/              POST                
* /login/               POST
* /user/users           GET
* /user/<id>/sleeps/     GET
* /user/<id>/sleeps/    POST
* /admin/  
