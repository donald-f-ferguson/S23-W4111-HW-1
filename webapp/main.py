# Simple starter project to test installation and environment.
# Based on https://fastapi.tiangolo.com/tutorial/first-steps/
#
from fastapi import FastAPI

# Explicitly included uvicorn to enable starting within main program.
# Starting within main program is a simple way to enable running
# the code within the PyCharm debugger
#
import uvicorn


from fastapi import FastAPI

# Added support for "static" web pages and other content.
#
from fastapi.staticfiles import StaticFiles

# Add package for returning HTML from routes
#
from fastapi.responses import HTMLResponse

# Used to add better type hints in intellisense and for generating
# OpenAPI documentation
#
from typing import List, Union
from pydantic import BaseModel

# Allows rendering the README.md as the root index page.
#
import markdown

# Implementation of the StudentResource and Data Transfer Object
#
from resources.StudentResource import StudentResource, StudentModel


app = FastAPI()

# See the explanation for static files and mount on the FastAPI documentation.
# https://fastapi.tiangolo.com/tutorial/static-files/
#
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index_page():
    """
    Returns the README.md as an HTML page.
    :return:
    """
    with open("README.md", "r") as in_file:
        result = in_file.read()
        result = markdown.markdown(result)

    return result


@app.get("/api/students")
async def get_student(name, dept_name) -> List[StudentModel]:
    """
    Returns information for all students. The next HW assignment will add support for
    query parameters.

    :return: A REST response with the info for all of the students
    """

    s = StudentResource()
    result = s.get_by_primary_key(None)
    return result


@app.get("/api/students/{ID}")
async def get_student(ID: str) -> StudentModel:
    """
    Get the resource for a specific student by the student ID.

    :param ID: The ID of the student.

    :return: A REST response with the student information.
    """

    s = StudentResource()
    result = s.get_by_primary_key(ID)
    return result



# Added the code below to enable running in PyCharm debugger.
# Modified the port from 8000 to 8001 because I often have multiple
# microservices running and need to spread over ports.
#
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)

