# S23-W4111-HW0

## Introduction

The top-level direction ```/web_app``` in the project 
[S23-W4111-HW0](https://github.com/donald-f-ferguson/S23-W4111-HW0) contains
a simple web application that tests the student's environment. Successfully testing
in HW0 simplifies completing the subsequent HW.

## Setup

To run the tests, you must:

- Setup a Python virtual environment in your integrated development environment (IDE).
Most students will use either VSCode or PyCharm for their IDEs. Use the online
documentation for your IDE to set up the interpreter/environment.


- Open a terminal window/command prompt from within your IDE. Following the IDE's
online instructions if you do not know how to open a terminal window/command
prompt.


- In the window, type ```pip install -r requirements.txt.```

## Running Tests

In the IDE, run the application ```.app.py.``` You should see something like the
following in the termina window.

<img src="static/img.png">

There are 2 basic tests:

1. [Health](./health) displays a simple health message.
2. [demo](./api/demo) "echoes" the HTTP operation and parameters.

You can run the tests but do not worry about what they do. We will discuss
in later lectures and recitations.

The final test accesses a database. To run the test, you must have:
- Installed MySQL Community Edition.
- Loaded the sample database.

The top-level HW Jupyter notebook provides instructions.

Running the test [Get Students](./api/students) should return something like

![img.png](/static/img2.png)