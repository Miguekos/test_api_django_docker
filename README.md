# Test API
This is a Django App

### Dependencies
- Django==3.2.6
- djangorestframework==3.12.4
- psycopg2==2.9.1

### How it works
```sh
$ docker-compose up -d --build
$ docker-compose run app python manage.py makemigrations
$ docker-compose run app python manage.py migrate
```

### Test
http://localhost:8000/api/worker
http://localhost:8000/api/worker/<id>

### Demo
```sh
- get_all
$ http://95.111.235.214:8002/api/worker

- create
$ http://95.111.235.214:8002/api/worker
POST
{    
    "first_name" : "Miguel",
    "last_name" : "Rodriguez",
    "function" : "Harvest"
}
```
### Response
````
{
    "id": 1,
    "first_name": "Miguel",
    "last_name": "Rodriguez",
    "function": "Harvest",
    "created_at": "2021-08-29T17:12:26.514915Z",
    "updated_at": "2021-08-29T17:12:26.514928Z"
}
````