import pymysql

from old.webapp.resources.BaseResource import BaseResource


class StudentResource(BaseResource):
    """
    This class implements the Student REST resource. It is a concrete implementation of the
    :class:`BaseResource`.

    Note: Putting SQL directly in a resource is a bad idea but we will do it for now.
    """

    def __init__(self):
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

    def get_by_primary_key(self, key):
        """

        :param key: Value for the primary key in db_book.student, which is ID.
        :return: A dictionary of {column_name, column_value}.
        """

        conn = StudentResource.get_connection()
        cur = conn.cursor()

        sql = "select * from db_book.student where ID=%s"
        res = cur.execute(sql, args=(key))
        result = cur.fetchall()

        """
        SQL queries ALWAYS return tables. This method returns an 'object.' So, we need to get the
        first element in the list. A list of length longer than 1 would be an error.
        """
        result = result[0]

        return result

