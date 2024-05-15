# django 1

## install python and pip

## install django
```shell
pip3 install django
```

## view version
```shell
python3 -m django --version
```

## create project
```shell
django-admin startproject projectName
```

## create database
```shell
python3 manage.py migrate
```

## run
```shell
python3 manage.py runserver
```

## db init
```shell
python3 manage.py makemigrations
```


__init__.py `一个空文件，告诉Python这个目录应该被认为是一个Python包。`
settings.py `Django 项目的配置文件。如果你想知道这个文件是如何工作的`
urls.py `Django 项目的 URL 声明，就像你网站的“目录”。`
asgi.py `作为您的项目在 ASGI 兼容的 Web 服务器上的入口运行`
wsgi.py `作为您的项目在 WSGI 兼容的 Web 服务器上运行的入口`