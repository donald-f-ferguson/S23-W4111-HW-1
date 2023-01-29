"""
Copyright @Donald F. Ferguson, 2023

This file is part of the application template for W4111, Section 002, Spring 21 HW assignments 3 and 4.

app.py is the 'main program.'

"""
import json

# DFF TODO -- Not critical for W4111, but should switch from print statements to logging framework.
from datetime import datetime

import markdown

#
# These packages provide functions for delivering a web application using Flask.
# Students can look online for education resources.
#
from flask import Flask, Response, request


import utils.rest_utils as rest_utils

from resources.StudentResource import StudentResource as StudentResource

# DFF TODO - We should not hardcode this here, and we should do in a context/environment service.
# OK for W4111 - This is not a course on microservices and robust programming.
#

#
# Create the Flask application object.
app = Flask(__name__)


##################################################################################################################

# DFF TODO This is a spectacularly bad way to provide this capability.
#
@app.route("/", methods=["GET"])
def index_page():

    with open("README.md", "r") as in_file:
        result = in_file.read()
        result = markdown.markdown(result)

    rsp = Response(result, status=200, content_type="text/html")
    return rsp


# DFF TODO A real service would have more robust health check methods.
# This path simply echoes to check that the app is working.
# The path is /health and the only method is GETs
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {
        "application": "S23-W4111-HW0",
        "status": "healthy",
        "time": str(datetime.now())
    }
    rsp_str = json.dumps(rsp_data, indent=2, default=str)
    rsp = Response(rsp_str, status=200, content_type="application/json")
    return rsp


# TODO Remove later. Solely for explanatory purposes.
# The method take any REST request, and produces a response indicating what
# the parameters, headers, etc. are. This is simply for education purposes.
#
@app.route("/api/demo/<parameter1>", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/api/demo/", methods=["GET", "POST", "PUT", "DELETE"])
def demo(parameter1=None):
    """
    Returns a JSON object containing a description of the received request.

    :param parameter1: The first path parameter.
    :return: JSON document containing information about the request.
    """

    # DFF TODO -- We should wrap with an exception pattern.
    #

    # Mostly for isolation. The rest of the method is isolated from the specifics of Flask.
    inputs = rest_utils.RESTContext(request, {"parameter1": parameter1})

    # DFF TODO -- We should replace with logging.
    r_json = inputs.to_json()
    msg = {
        "/demo received the following inputs": inputs.to_json()
    }
    print("/api/demo/<parameter> received/returned:\n", msg)

    rsp = Response(json.dumps(msg,  indent=2, default=str), status=200, content_type="application/json")
    return rsp


@app.route("/api/students/", methods=["GET"])
def get_students():

    result = StudentResource.get_students()
    rsp = Response(json.dumps(result,  indent=2, default=str), status=200, content_type="application/json")
    return rsp


##################################################################################################################
# Actual routes begin here.
#


if __name__ == '__main__':

    # DFF TODO We will handle host and SSL certs different in deployments.
    app.run(host="0.0.0.0", port=5001)
