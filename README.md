# Python: Killian

A barebones Django app for Dekoruma to be cloned and renamed, which can easily be deployed to Heroku.

## Setup

```sh
$ make install
```

## Running Locally

```sh
$ pipenv shell
$ python manage.py runserver
```

Your app should now be running on [localhost:9999](http://localhost:9999/).

## Run Management Commands

1. Add a python file in killian/management/commands/
2. Create command class
3. Run your script files using `python manage.py {name_of_your_python_file}`

## What Should be Replaced for Creating New Service

1.  Update its **.env** file [Secret Key Generator](https://www.miniwebtool.com/django-secret-key-generator/)
2.  Replace the name of its **main folder**
3.  Replace the default port in **manage.py** file, avoid using port that is already in use [List Microservices Dekoruma](https://quip.com/eJFyAaanfn0s)
4.  Update the default port and other info in **README.md** file
5.  Replace name of _PROJECT_APPS_ **settings.py** file
6.  List this service on [List Micorservices Dekoruma](https://quip.com/eJFyAaanfn0s)
7.  Add wiki docs for this service [Template Wiki](https://quip.com/gAHlASBWEVLK)
