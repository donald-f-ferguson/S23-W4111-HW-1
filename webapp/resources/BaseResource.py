from typing import List, Union

from fastapi import FastAPI
from abc import ABC, abstractmethod


class BaseResource(ABC):
    """
    This is am abstract base class for classes implementing a REST Resource. We will flesh this out later in the
    semester.
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_by_primary_key(self, key):
        """
        Retrieve a resource by the 'primary key.' This supports paths of the form /ResourceName/primary_key. An
        example would be /students/dff9.

        :param key: The primary key.
        :return: A dictionary of the form {key, value} containing the resource properties. For /students/dff9, this
            might be something like
                {
                    "uni": "dff9",
                    "last_name": "Ferguson",
                    "first_name": "Donald"
                }
            Returns None if the resource does not exist.
        """
        pass

