# Project Django - compraencasa

Is an application that consists of a simple search, showing the result if it is found.

## Dependencies
- docker
- docker-compose


## Installation
```sh
git clone https://github.com/frabrusco/project-comparaencasa.git
cd project-compraencasa
docker-compose up
```
> Note that you have to leave ports 3306 for mysql and 8000 for django app free.

## Add an element
When mysql and django servers are up.
First we see the name of the django container.
```sh
docker ps
```
Then run
```sh
docker exec name-container-django python manage.py addcars car-plate car-name
```

## Search elements
- Open web browser and go to url http://0.0.0.0:8000/
- Put a car plate in the input
- Then press search

## Test 
Run tests
```sh
docker exec name-container-django python manage.py test
```

## Build with
- django
- mysql
- docker
- docker-compose
