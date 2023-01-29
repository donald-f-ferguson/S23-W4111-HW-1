import pymysql
from pydantic import BaseModel

from webapp.resources.BaseResource import BaseResource


class StudentModel(BaseModel):
    """
    Data Transfer Object for student data.
    """
    ID: str = None
    name: str = None
    dept_name: str = None
    tot_cred: int = None


class StudentResource(BaseResource):
    """
    This class implements the Student REST resource. It is a concrete implementation of the
    :class:`BaseResource`.

    Note: Putting SQL directly in a resource is a bad idea but we will do it for now.
    """

    def __init__(self, ID=None, name=None, dept_name=None, tot_cred=None):
        super().__init__()

    @staticmethod
    def get_connection():
        """
        Get a database connection. DB specific code should not be in the resource. Also, different types of
        database will have different approaches to connecting. So, we would be abstract classes for specific
        databases and database types. We will improve the code during the semester.
        :return: a pymysql.Connection.
        """

        """
        TODO: DO NOT PUT USER ID, PASSWORD OR OTHER SECURITY INFORMATION IN CODE.
        
        There are design patterns for passing secure information to applications.
        
        For this class, replace the user and password to what you chose for MySQL.
        
        Also, this method should be protected.
        """
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="dbuserdbuser",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn

    def get_by_primary_key(self, key=None):
        """

        :param key: Value for the primary key in db_book.student, which is ID. If the value is None,
            it returns all resources in the collection.
        :return: None, the single StudentModel or List[StudentModel]
        """

        conn = StudentResource.get_connection()
        cur = conn.cursor()

        if key:
            sql = "select * from db_book.student where ID=%s"
        else:
            sql = "select * from db_book.student"

        res = cur.execute(sql, args=(key))
        result = cur.fetchall()

        """
        SQL queries ALWAYS return tables. This method may return  an 'object.' So, we need to get the
        first element in the list. A list of length longer than 1 would be an error.
        """
        if key:
            if result:
                result = StudentModel(**result[0])
            else:
                result = []
        else:
            [StudentModel(**s) for s in result]

        return result

    def get_by_query(self, name=None, dept_name=None):
        """

        Performs a SQL query to return students based on name, dept_name or both. To complete this part of the
        HW, the programming track student must form an SQL query performs the equivalent query on the database.
        For example, if only the name parameter is not None and has value "Bob", the query would be

        select * from db_book.student where name='Bob'. The preceding method get_by_primary_key shows how to
        form and submit SQL queries.

        :param name: The name of the student in db_book.student.
        :param dept_name: The dept_name in db_book.student
        :return: All students making the query.
        """

        # Delete the line below after you have implemented the function.
        #
        raise NotImplemented()

        #
        # Your code goes here



