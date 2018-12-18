# django-project-skeleton
Django Project Skeleton

## Create django project
```sh
django-admin startproject --template https://github.com/hotbaby/django-project-skeleton/archive/master.zip --name pytest.ini project-name
```

OR

```sh
wget https://github.com/hotbaby/django-project-skeleton/archive/master.zip && django-admin startproject --template file://$PWD/master.zip --name pytest.ini project && rm -f master.zip
```