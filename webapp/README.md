# S23-W4111-HW1: Programming Track Web Application

## Introduction

The top-level direction ```/web_app``` in the project 
[S23-W4111-HW-1](https://github.com/donald-f-ferguson/S23-W4111-HW-1) contains
the core of a web application that programming track students will expand in homework
assignments.

## Setup

To run the tests, you must:

- Setup a Python virtual environment in your integrated development environment (IDE).
Most students will use either VSCode or PyCharm for their IDEs. Use the online
documentation for your IDE to set up the interpreter/environment.


- Open a terminal window/command prompt from within your IDE. Following the IDE's
online instructions if you do not know how to open a terminal window/command
prompt.


- In the window, type ```pip install -r requirements.txt.```

## Starting the Web Application

In the IDE, run the application ```main.py.``` You should see something like the
following in the terminal window.

<img src="https://donald-f-ferguson.github.io/Intro_to_Databases_S23/images/webapp-start.png">


## Tests

REST applications implement [resources](https://restfulapi.net/). A URL identifies/locates a resource.
The first part of the URL, e.g. ```localhost:8002```, locates the server program implementing the
resources. The second part of the URL is a [path](https://restfulapi.net/resource-naming/) that locates
the resource in the server.

There are several basic tests to check the application and it's routes.

1. [Home Page](./) displays this README.md as an HTML page.
2. [docs](./docs) returns the [OpenAPI](https://www.openapis.org/) page for the application.


The final test accesses a database. To run the test, you must have:
- Installed MySQL Community Edition.
- Loaded the sample database.

You performed these tasks in HW 0.

For the final test,
1. Go to the [docs](./docs)
2. Click on ```GET /api/students/{ID}```
3. Click on ```Try it out```
4. Enter ```12345``` in the entry field for ID.
5. Click execute and scroll down. 

You should see something like ... ...

<img src="https://donald-f-ferguson.github.io/Intro_to_Databases_S23/images/openapi-execute.png">

## Complete

Your setup test is complete. Please follow the instructions in the notebook for completing the
programming track tasks.