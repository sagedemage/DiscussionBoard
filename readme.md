# Discussion Board

[![Production Workflow](https://github.com/sagedemage/final_flask_start/actions/workflows/prod.yml/badge.svg)](https://github.com/sagedemage/final_flask_start/actions/workflows/prod.yml)
* [Production Deployment](https://discussion-board-prod.herokuapp.com/)

[![Development Workflow](https://github.com/sagedemage/final_flask_start/actions/workflows/dev.yml/badge.svg)](https://github.com/sagedemage/final_flask_start/actions/workflows/dev.yml)
* [Development Deployment](https://discussion-board-dev.herokuapp.com/)

## About

This is the flask web application for Project 4.

## Purpose

* The purpose of the web application is to create an environment for anyone to post their opinions
or areas of interest on the discussion board.  It is very opened ended.
  * For example, people can post about their favorite movies, video games or sports team.
* The content the users add to the discussion board adds value for other users viewing this web 
  application. Users can get information and learn from other users. The web app does not have the ability for users to react or reply to
  people's posts.

## Environmental Variables
Fill in the environmental variables in .env.test file

## Setting up the docker container of the web applicaiton
Build the docker container:
````
docker-compose build
````
Start the docker container:
````
docker-compose up -d
````
To access the docker container shell:
````
docker exec -it $(docker ps -q) /bin/bash
````

## Unit testing the web application
Access the docker container shell:
````
docker exec -it $(docker ps -q) /bin/bash
````
Remove the database with data if it has data in it:
````
rm database/db.sqlite
````
Then create a new empty database:
````
flask create-db
````
